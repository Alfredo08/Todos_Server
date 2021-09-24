
function closeSession( event ){
    let URL = '/logout';
    let settings = {
        method : 'GET'
    }

    fetch( URL, settings )
        .then( response => {
            if( response.ok ){
                return response.json();
            }
            // Handle the error here in case there is any
        })
        .then( data => {
            console.log( data );
            window.location.href = "/login";
        });
}

logoutButton = document.querySelector( '.logout' );
logoutButton.addEventListener( 'click', closeSession )