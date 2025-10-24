// Minimal client-side validation for contact form
// Ensures accessibility by updating inline error regions with aria-live

(function () {
  const form = document.getElementById('contactForm');
  if (!form) return;

  const fields = {
    firstName: {
      input: document.getElementById('firstName'),
      error: document.getElementById('firstNameError'),
      validate: (v) => v.trim().length > 0 || 'First name is required.'
    },
    lastName: {
      input: document.getElementById('lastName'),
      error: document.getElementById('lastNameError'),
      validate: (v) => v.trim().length > 0 || 'Last name is required.'
    },
    email: {
      input: document.getElementById('email'),
      error: document.getElementById('emailError'),
      validate: (v) => /.+@.+\..+/.test(v) || 'Enter a valid email address.'
    },
    password: {
      input: document.getElementById('password'),
      error: document.getElementById('passwordError'),
      validate: (v) => (v && v.length >= 8) || 'Password must be at least 8 characters.'
    },
    confirmPassword: {
      input: document.getElementById('confirmPassword'),
      error: document.getElementById('confirmPasswordError'),
      validate: (v) => v === document.getElementById('password').value || 'Passwords must match.'
    }
  };

  function setError(fieldKey, message) {
    const { input, error } = fields[fieldKey];
    if (message === true) message = '';
    if (message) {
      input.setAttribute('aria-invalid', 'true');
      error.textContent = message;
    } else {
      input.removeAttribute('aria-invalid');
      error.textContent = '';
    }
  }

  function validateField(fieldKey) {
    const { input, validate } = fields[fieldKey];
    const result = validate(input.value);
    setError(fieldKey, result === true ? '' : result);
    return result === true;
  }

  Object.keys(fields).forEach((key) => {
    const { input } = fields[key];
    input.addEventListener('blur', () => validateField(key));
    input.addEventListener('input', () => setError(key, ''));
  });

  form.addEventListener('submit', (e) => {
    let allValid = true;
    Object.keys(fields).forEach((key) => {
      const valid = validateField(key);
      if (!valid) allValid = false;
    });
    if (!allValid) {
      e.preventDefault();
      const firstInvalid = Object.keys(fields).map((k) => fields[k]).find((f) => f.input.getAttribute('aria-invalid') === 'true');
      if (firstInvalid) firstInvalid.input.focus();
    }
    // On valid submit: allow navigation to thankyou.html via form action
  });
})();


