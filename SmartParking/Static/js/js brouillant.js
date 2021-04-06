/*$(function aj(user_id,arrived){$.ajax({
 	       url:"update_reservation/{{delta.id}}",
 	       type: 'POST'
         	 data : {
           	'user':user_id,
         	'arrived': arrived,
         	'R': false,}

     	 });
		});*/
	/**/
/*
			
     	 var url = "update_reservation/{{delta.id}}",
     	 fetch(url, {
				method:'POST',
			body:JSON.stringify({'user':user_id,
         	'arrived': arrived,
         	'R': false,})

		})*/

axios({
	      method: 'post',
	      url:'update_reservation/{{delta.id}}/',
	      data: {
			user:user_id,
         	arrived: arrived,
         	R: false,
	      },
	      validateStatus: (status) => {
	        return true; // I'm always returning true, you may want to do it depending on the status received
	      },
	    }).catch(error => {
	    	 console.log(error);
	    }).then(response => {
	        // this is now called!
	         console.log(response);
	    });
