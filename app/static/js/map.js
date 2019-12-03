function initMap() {
     var map = new google.maps.Map(document.getElementById('map'), {
          center: {lat: 42.3314, lng: -83.0458},
          zoom: 13
        });

        var card = document.getElementById('pac-card');
        var input = document.getElementById('pac-input');
        var types = document.getElementById('type-selector');
        var strictBounds = document.getElementById('strict-bounds-selector');
        map.controls[google.maps.ControlPosition.TOP_RIGHT].push(card);
        var autocomplete = new google.maps.places.Autocomplete(input);
        // Bind the map's bounds (viewport) property to the autocomplete object,
        // so that the autocomplete requests use the current map bounds for the
        // bounds option in the request.
        autocomplete.bindTo('bounds', map);
        // Set the data fields to return when the user selects a place.
        autocomplete.setFields(
            ['address_components', 'geometry', 'icon', 'name']);

        var infowindow = new google.maps.InfoWindow();
        var infowindowContent = document.getElementById('infowindow-content');
        infowindow.setContent(infowindowContent);
        var marker = new google.maps.Marker({
          map: map,
          anchorPoint: new google.maps.Point(0, -29)
        });
        autocomplete.addListener('place_changed', function() {
          infowindow.close();
          marker.setVisible(false);
          var place = autocomplete.getPlace();
          if (!place.geometry) {
            // User entered the name of a Place that was not suggested and
            // pressed the Enter key, or the Place Details request failed.
            window.alert("No details available for input: '" + place.name + "'");
            return;
          }
          // If the place has a geometry, then present it on a map.
          if (place.geometry.viewport) {
            map.fitBounds(place.geometry.viewport);
          } else {
            map.setCenter(place.geometry.location);
            map.setZoom(17);  // Why 17? Because it looks good.
          }
          marker.setPosition(place.geometry.location);
          marker.setVisible(true);
          var address = '';
          if (place.address_components) {
            address = [
              (place.address_components[0] && place.address_components[0].short_name || ''),
              (place.address_components[1] && place.address_components[1].short_name || ''),
              (place.address_components[2] && place.address_components[2].short_name || '')
            ].join(' ');
          }
          infowindowContent.children['place-icon'].src = place.icon;
          infowindowContent.children['place-name'].textContent = place.name;
          infowindowContent.children['place-address'].textContent = address;
          infowindow.open(map, marker);
        });
        // Sets a listener on a radio button to change the filter type on Places
        // Autocomplete.
        function setupClickListener(id, types) {
          var radioButton = document.getElementById(id);
          radioButton.addEventListener('click', function() {
            autocomplete.setTypes(types);
          });
        }
        setupClickListener('changetype-all', []);
        setupClickListener('changetype-address', ['address']);
        setupClickListener('changetype-establishment', ['establishment']);
        setupClickListener('changetype-geocode', ['geocode']);
        document.getElementById('use-strict-bounds')
            .addEventListener('click', function() {
              console.log('Checkbox clicked! New state=' + this.checked);
              autocomplete.setOptions({strictBounds: this.checked});
            });

        var image = 'https://developers.google.com/maps/documentation/javascript/examples/full/images/beachflag.png';
        //(1) Hopcat
        var hopcat = new google.maps.Marker({
            position: {lat: 42.352685, lng: -83.061536},
            map: map,
            icon: image,
            title: 'Hopcat'
        });
        //InfoWindow (Hopcat)
        //(2) Majestic Theater
        var majestic = new google.maps.Marker({
            position: {lat: 42.351673, lng: -83.060076},
            map: map,
            icon: image
        });
        //(3) Welcome Center
        var welcome = new google.maps.Marker({
            position: {lat: 42.357242, lng: -83.065131},
            map: map,
            icon: image
        });
        //(4) La Pita
        var pita = new google.maps.Marker({
            position: {lat: 42.357240, lng: -83.066208},
            map: map,
            icon: image
        });
        //(5) Eastern Market
        var market = new google.maps.Marker({
            position: {lat: 42.347381, lng: -83.040503},
            map: map,
            icon: image
        });
        //(6) Detroit Opera House
         var opera = new google.maps.Marker({
            position: {lat: 42.336469, lng: -83.048638},
            map: map,
            icon: image
        });
         //(7) LCA
         var arena = new google.maps.Marker({
            position: {lat: 42.341234, lng: -83.055048},
            map: map,
            icon: image
        });
         //(8) Whole Foods
         var grocery = new google.maps.Marker({
            position: {lat: 42.348660, lng: -83.056608},
            map: map,
            icon: image
        });
         //(9) MoCAD
         var museum = new google.maps.Marker({
            position: {lat: 42.353882, lng: -83.061874},
            map: map,
            icon: image
        });
         //(10) Selden Standard
         var restaurant = new google.maps.Marker({
            position: {lat: 42.348054, lng: -83.064964},
            map: map,
            icon: image
        });
         //(11) Parc
         var restaurant = new google.maps.Marker({
            position: {lat: 42.331824, lng: -83.064964},
            map: map,
            icon: image
        });
}