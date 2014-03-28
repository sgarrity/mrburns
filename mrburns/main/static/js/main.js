console.log('I bring you love!');

$( '.stats-panel-tab' ).click(function() {
    $( '.stats-panel' ).toggleClass( "open" );
});

$( '#choice' ).modal(choiceOptions);

var choiceOptions = {
    "show" : "true"
}
