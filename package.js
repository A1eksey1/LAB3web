Package.describe({
  name: 'comerc:autoform-nativemultiple',
  summary: 'Custom "nativemultiple" input type for AutoForm',
  version: '0.0.1',
  git: 'https://github.com/comerc/meteor-autoform-nativemultiple.git'
});

Package.onUse(function(api) {
  api.versionsFrom('1.0');
  api.use('templating@1.0.0');
  api.use('blaze@2.0.0');
  api.use('aldeed:autoform@4.0.0');
  api.addFiles([
    'autoform-nativemultiple.html',
    'autoform-nativemultiple.js',
  ], 'client');
});
