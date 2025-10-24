#!/usr/bin/env python3
"""
Test script to verify Flask application functionality
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

def test_flask_app_creation():
    """Test that Flask app can be created"""
    try:
        from app import app
        assert app is not None, "Flask app should be created"
        assert app.name == "app", "App name should be 'app'"
        print("✅ Flask app created successfully")
        return True
    except Exception as e:
        print(f"❌ Flask app creation failed: {e}")
        return False

def test_flask_routes():
    """Test that Flask routes are configured"""
    try:
        from app import app
        routes = [str(rule) for rule in app.url_map.iter_rules()]
        expected_routes = ['/', '/about', '/resume', '/projects', '/contact', '/addproject', '/thankyou']
        
        for route in expected_routes:
            assert route in routes, f"Route {route} should be configured"
        
        print("✅ All Flask routes configured correctly")
        print(f"✅ Found {len(routes)} routes total")
        return True
    except Exception as e:
        print(f"❌ Flask routes test failed: {e}")
        return False

def test_project_data_structure():
    """Test that project data has correct structure"""
    try:
        from DAL import getAllProjects
        projects = getAllProjects()
        
        for project in projects:
            assert 'Title' in project, "Project should have Title field"
            assert 'Description' in project, "Project should have Description field"
            assert 'Image' in project, "Project should have Image field"
            assert isinstance(project['Title'], str), "Title should be string"
            assert isinstance(project['Description'], str), "Description should be string"
            assert isinstance(project['Image'], str), "Image should be string"
        
        print("✅ Project data structure is correct")
        return True
    except Exception as e:
        print(f"❌ Project data structure test failed: {e}")
        return False

def test_projects():
    """Main test function for projects"""
    print("Testing Flask application and project functionality...")
    
    # Test Flask app
    app_ok = test_flask_app_creation()
    
    # Test routes
    routes_ok = test_flask_routes()
    
    # Test data structure
    data_ok = test_project_data_structure()
    
    if app_ok and routes_ok and data_ok:
        print("🎉 All project tests passed!")
        return True
    else:
        print("❌ Some project tests failed!")
        return False

if __name__ == "__main__":
    test_projects()
