function myfunc() {
    let isitme;
    isitme = function () {
        return "it's a me, mario";
    };

    console.log(isitme());

    isitme = function() {
        return "it's a me, luigi";
    }
}

myfunc()
