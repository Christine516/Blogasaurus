

//creating new entry when hitting submit button
// i used this link :https://www.w3schools.com/jsref/tryit.asp?filename=tryjsref_text_get


function printEntry(){
  let userinput = document.getElementById("textbox").value;
    if (userinput != " ")
      document.getElementById("entry").innerHTML = userinput

}
