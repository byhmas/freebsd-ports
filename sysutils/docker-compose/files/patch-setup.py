--- setup.py.orig	2019-02-04 16:11:53 UTC
+++ setup.py
@@ -33,8 +33,8 @@ install_requires = [
     'cached-property >= 1.2.0, < 2',
     'docopt >= 0.6.1, < 0.7',
     'PyYAML >= 3.10, < 4.3',
-    'requests >= 2.6.1, != 2.11.0, != 2.12.2, != 2.18.0, < 2.21',
-    'texttable >= 0.9.0, < 0.10',
+    'requests >= 2.6.1, != 2.11.0, != 2.12.2, != 2.18.0, < 3',
+    'texttable >= 0.9.0, < 2',
     'websocket-client >= 0.32.0, < 1.0',
     'docker[ssh] >= 3.7.0, < 4.0',
     'dockerpty >= 0.4.1, < 0.5',
