start() {
    echo "Application is starting. If image is not built already it will be build."

    docker compose up -d
}

build() {
    docker build -t infinity .
}


while true; do

    printf "Select an action :\n1) Start Application \n2) Stop Application \n3) Build Application\n"
    read -p "Type your selection: " component
    case $component in
        [1]* )
            start
            docker-compose ps
        	break;;
        [2]* ) 
			docker-compose down
			break;;
		[3]* ) 	
            build
			break;;                      
        * ) echo "Please type one of the above.";;
    esac
done
