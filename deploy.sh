./build.sh
ssh stefano@51.210.12.70 "rm -rf /var/www/stefanopace"
scp -r build/curriculum stefano@51.210.12.70:/var/www/stefanopace
