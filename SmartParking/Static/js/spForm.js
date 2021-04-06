const nom=document.getElementById('nom');
const prenom=document.getElementById('prenom');
const numBadge=document.getElementById('numBadge');
const phone=document.getElementById('phone');
const voiture =document.getElementById('voiture');
const matricule=document.getElementById('matricule');
const mail =document.getElementById('mail');
const pw=document.getElementById('pw');
const confpw=document.getElementById('confpw');


/*function insubmit() {
	const formsub=document.getElementById(subForm);
	formsub.onsubmit=function(e){e.preventDefault();}
}*/
const spanErpw=document.getElementById('pwcdt');
function pwLength()
{ 
	if(pw.value.length<6)
	{
		spanErpw.innerHTML=" Le nombre de caractères saisi est insuffisant";
		spanErpw.style.color='rgb(255,0,0)';
		pw.style.border='rgb(255,0,0) 1px solid';
	}
	else{
		spanEr.innerHTML=" ";
		confpw.style.border='#a9a9a9 1px solid';
	}
}
const spanEr=document.querySelector("#pwconfError");
/*confpw.onblur=*/function comparaison ()
{
	if (pw.value!==confpw.value)
	{	
		spanEr.innerHTML="Veuillez ressaisir votre mot de passe";
		spanEr.style.color='rgb(255,0,0)';
		confpw.style.border='rgb(255,0,0) 1px solid';
		//insubmit();
	}	
	else{
		spanEr.innerHTML=" ";
		confpw.style.border='#a9a9a9 1px solid';
		//spanEr.style.color='rgb(0,255,0)';
	}
}

confpw.addEventListener('blur',comparaison);
pw.addEventListener('change',comparaison);
pw.addEventListener('change',pwLength);
pw.addEventListener('blur',pwLength);
