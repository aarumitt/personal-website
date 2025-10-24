#!/usr/bin/env python3
"""
Test script to verify database functionality
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from DAL import *

def test_database_connection():
    """Test basic database connection and operations"""
    try:
        # Test getting all projects
        projects = getAllProjects()
        assert isinstance(projects, list), "getAllProjects should return a list"
        print("✅ Database connection successful")
        print(f"✅ Found {len(projects)} projects in database")
        return True
    except Exception as e:
        print(f"❌ Database connection failed: {e}")
        return False

def test_database_operations():
    """Test database CRUD operations"""
    try:
        # Test adding a project
        test_title = "Test Project"
        test_description = "This is a test project"
        test_image = "test.png"
        
        # Save project
        saveProjectDB(test_title, test_description, test_image)
        print("✅ Project saved successfully")
        
        # Retrieve projects
        projects = getAllProjects()
        test_project = next((p for p in projects if p['Title'] == test_title), None)
        assert test_project is not None, "Test project should be found"
        assert test_project['Description'] == test_description, "Description should match"
        print("✅ Project retrieval successful")
        
        # Clean up - delete test project
        deleteProjectDB(test_title)
        print("✅ Test project cleaned up")
        
        return True
    except Exception as e:
        print(f"❌ Database operations failed: {e}")
        return False

def test_database():
    """Main test function"""
    print("Testing database functionality...")
    
    # Test connection
    connection_ok = test_database_connection()
    
    # Test operations
    operations_ok = test_database_operations()
    
    if connection_ok and operations_ok:
        print("🎉 All database tests passed!")
        return True
    else:
        print("❌ Some database tests failed!")
        return False

if __name__ == "__main__":
    test_database()
