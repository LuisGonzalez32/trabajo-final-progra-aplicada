function hideDivById(divId) {
    hideAllDivW3Includes()
    var element = document.getElementById(divId)
    if (element.style.display === "none") {
        element.style.display = "block";
    }
}

function hideAllDivW3Includes() {
    var elementArray = document.getElementsByName("pages")
    for (var element of elementArray) {
        element.style.display = "none"
    }
}



function registerNewUser() {
    var reg_user = document.getElementById("user_reg").value;
    var reg_password = document.getElementById("passw_reg").value;
    var reg_role = "client";

    var userArray = [];

    if (localStorage.getItem("lUserArray") !== null) {
        userArray = JSON.parse(localStorage.getItem("lUserArray"));
    }

    var current_reg = {
        user: reg_user,
        password: reg_password,
        role: reg_role
    };

    userArray.push(current_reg);

    localStorage.setItem("lUserArray", JSON.stringify(userArray));

    window.location.href = "logIn";
}

function loginMenu() {
    var radios = document.getElementsByName('loginMenu');
    for (var i = 0, length = radios.length; i < length; i++) {
        if (radios[i].checked) {
            element = radios[i].value;
            if (element === "logIn") {
                window.location.href = "logIn";
            }
            else {
                window.location.href = "createAccount";
            }
            break;
        }
    }
}

function checkLogin() {
    var user = document.getElementById("user").value;
    var password = document.getElementById("passw").value;

    var userArray = JSON.parse(localStorage.getItem("lUserArray"));

    if (user !== null && user !== "") {
        if (password !== null && password !== "") {
            var canLogin = checkLoginInfo(user, password, userArray);

            if (canLogin === true) {
                var role = getUserRole(user, password, userArray)

                createSessionUser(user, password, role)
                if (role === "admin") {
                    window.location.href = "adminDashboard";
                }
                else {
                    window.location.href = "dashboard";
                }
            } else {
                alert("user or password are not correct");
            }
        } else {
            alert("password must not be empty");
        }
    } else {
        alert("user must not be empty");
    }
}

function checkLoginInfo(user, password, userArray) {
    if (userArray !== null && userArray.length > 0) {
        for (var i = 0; i < userArray.length; i++) {
            if (userArray[i].user === user && userArray[i].password === password) {
                return true;
            }
        }
    }
    return false;
}

function getUserRole(pUser, pPassword, pUserArray) {
    var role = ""
    if (pUserArray !== null && pUserArray.length > 0) {
        var length = pUserArray.length
        for (var i = 0; i < length; i++) {
            if (pUserArray[i].user === pUser && pUserArray[i].password === pPassword) {
                role = pUserArray[i].role
                break
            }
        }
    }
    return role
}

function createSessionUser(user, password, role) {
    var logged_user = {
        user: user,
        password: password,
        role: role
    };
    sessionStorage.setItem("loggedUser", JSON.stringify(logged_user));
}


//--------------------------------------------------------------------------------------------------------------------
function checkSession() {
    checkForValidLoginSession()
    w3.includeHTML()
}

function checkForValidLoginSession() {

    if (sessionStorage.getItem("loggedUser") == null) {
        window.location.href = "logIn"
    }
}

function setUserNameOnDashboard() {
    var sessionUserArray = JSON.parse(sessionStorage.getItem("loggedUser"))
    var currentUser = sessionUserArray.user
    var currentRole = sessionUserArray.role

    var userSpan = document.getElementById("sessionUser")
    userSpan.innerText = "Hello, " + currentRole + " " + currentUser
}

function logout() {
    sessionStorage.removeItem("loggedUser")
    hideDivById("loginMenu");
}


//----------------------------------------------------------------------------------------------------------------------------------

function displayRooms(capacity) {

    hideDivById('rooms');
    checkSession();
    setUserNameOnDashboard()

    var roomsArray = JSON.parse(localStorage.getItem("lRoomsArray"));

    for (var i = 0, length = roomsArray.length; i < length; i++) {

        var element = document.getElementById("room" + i);
        if (element) {
            element.parentNode.removeChild(element);
        }

        if (roomsArray[i].capacity == capacity) {
            var para = document.createElement("li");
            room = roomsArray[i].name
            var node = document.createTextNode(room);
            para.appendChild(node);
            var si = document.createElement("br");
            para.appendChild(si)
            room1 = "price: $" + roomsArray[i].price
            var room2 = document.createTextNode(room1);
            para.appendChild(room2);
            var sii = document.createElement("br");
            para.appendChild(sii)
            room2 = "balcon: " + roomsArray[i].balcon
            var room3 = document.createTextNode(room2);
            para.appendChild(room3);
            var element = document.getElementById("li1").appendChild(para);

            var button = document.createElement("button");
            button.innerHTML = "Book room"
            button.setAttribute("id", "room" + i)
            para.setAttribute("id", "room" + i)
            button.setAttribute("onclick", "bookingRoom(id, " + roomsArray[i].price + ")")
            element.appendChild(button)
        }
    }

    document.getElementById("roomBooking").addEventListener("click", function () {
        displayRooms(capacity)
    });
}

function bookingRoom(id, price) {
    hideDivById("dateBooking")
    var i = 0
    document.getElementById("bookRoomButton").addEventListener("click", function () {
        if (i == 0) {

            bookingDates(id, price)
            i++
        }
    });
}

function displayFood(capacity) {

    hideDivById('food');
    checkSession();

    var services = JSON.parse(localStorage.getItem("services"));

    for (var i = 0, length = services.length; i < length; i++) {

        var element1 = document.getElementById("food" + i);
        if (element1) {
            element1.parentNode.removeChild(element1);
        }

        var para = document.createElement("li");
        para.innerHTML = services[i].food
        var element = document.getElementById("li11").appendChild(para);

        var button = document.createElement("button");
        button.innerHTML = "Order"
        button.setAttribute("id", "food" + i)
        para.setAttribute("id", "food" + i)
        button.setAttribute("onclick", 'foodBookedArray( " ' + services[i].food + ' " )');
        element.appendChild(button)
    }
}

function foodBookedArray(food1) {

    var foodArray = [];

    if (localStorage.getItem("servicesBooked") !== null) {
        foodArray = JSON.parse(localStorage.getItem("servicesBooked"));
    }

    var name1 = loadUserName()

    var now = new Date();

    var current_reg = {
        name: name1,
        date: now,
        food: food1
    };

    foodArray.push(current_reg);

    localStorage.setItem("servicesBooked", JSON.stringify(foodArray));

    alert("la orden ha sido guardada")
}

function bookingDates(Id, price) {

    var time1 = new Date(document.getElementById("checkIn").value);
    var time2 = new Date(document.getElementById("checkOut").value);

    roomArray = JSON.parse(localStorage.getItem("lRoomsBookedArray"));

    if (roomArray[Id].length >= 1) {

        time1 = JSON.stringify(time1)
        time2 = JSON.stringify(time2)

        var a = false

        var i
        for (i = 0; i < roomArray[Id].length; i++) {

            if (roomArray[Id][i] != null) {
                var checkIn = JSON.stringify(roomArray[Id][i].checkIn)
                var checkOut = JSON.stringify(roomArray[Id][i].checkOut)

                if (time1 <= checkIn && time2 >= checkOut) {
                    a = true
                } else if (time1 <= checkOut && time2 >= checkIn) {
                    a = true
                }
            }
        }
        if (a == false) {
            registerBooking(Id, time1, time2, price)
            alert("la reserva se realizo con exito")
        } else {
            alert("Ya hay reservacion para ese dia")
        }
    }
    else {
        if (time2 > time1) {
            registerBooking(Id, time1, time2, price)
            alert("La reserva se realizo con exito")
        }
        else {
            alert("no puede hacer checkIn despues del checkOut")
        }
    }
}

function registerBooking(Id, date1, date2, price) {
    if (localStorage.getItem("lRoomsBookedArray") !== null) {
        var roomArray = [];

        roomArray = JSON.parse(localStorage.getItem("lRoomsBookedArray"));
    }

    var name = loadUserName()

    var arraynew = {
        nombre: name,
        checkIn: date1,
        checkOut: date2,
        price1: price
    };

    roomArray[Id].push(arraynew);

    localStorage.setItem("lRoomsBookedArray", JSON.stringify(roomArray));
}

function loadUserName() {
    var name
    if (sessionStorage.getItem("loggedUser") !== null) {
        name = JSON.parse(sessionStorage.getItem("loggedUser"));

        return name.user
    }
}
//-------------------------------------------------------------------------------------------------------------------------

function roomCapacity() {
    var radios = document.getElementsByName('checkCapacity');
    for (var i = 0, length = radios.length; i < length; i++) {
        if (radios[i].checked) {
            displayRooms(radios[i].value)
        }
    }
}

function clientMenu() {
    checkSession();
    hideDivById('clientMenu');
}

function allReservations() {

    var rowCount = document.getElementById("myTable").rows.length;

    if (rowCount > 1) {
        deleteReservationsTable(rowCount)
        insertTable()
    }
    else {
        insertTable()
    }
}



function insertTable() {

    roomArray = JSON.parse(localStorage.getItem("lRoomsBookedArray"));

    room = JSON.parse(localStorage.getItem("lRoomsArray"));

    var user = JSON.parse(sessionStorage.getItem("loggedUser"));

    var i = 0

    var total = 0

    while (i < 6) {
        if (roomArray["room" + i].length > 0) {

            hideDivById("myReservations")

            for (e = 0; e < roomArray["room" + i].length; e++) {

                if (roomArray["room" + i][e] != null) {

                    if (user.role == "client") {
                        if (user.user == roomArray["room" + i][e].nombre) {
                            table(roomArray, user, i, e)
                            total = total + roomArray["room" + i][e].price1
                        }
                    }
                    else {
                        table(roomArray, user, i, e)
                        total = total + roomArray["room" + i][e].price1
                    }
                }
            }
        }
        i++
    }

    if (document.getElementById("li3") === null) {
        var para = document.createElement("li");
        para.setAttribute("id", "li3")
        room = "Total: $" + total
        var node = document.createTextNode(room);
        para.appendChild(node);
        var element = document.getElementById("li2").appendChild(para);
    }
    else {
        doc = document.getElementById("li3")
        doc.innerHTML = "Total: $" + total
    }

}


function deleteReservationsTable(row) {

    var id = document.getElementById("")

    while (row !== 1) {
        document.getElementById("myTable").deleteRow(1);
        row--
    }
}

function deleteAllFoodTable(row) {

    while (row !== 1) {
        document.getElementById("myFoodTable").deleteRow(1);
        row--
    }
}



function table(roomArray, user, i, e) {

    var table = document.getElementById("myTable");

    var newRow = table.insertRow(1);

    newRow.setAttribute("name", "reservation00")

    newRow.setAttribute("class", "active-row")

    var cell1 = newRow.insertCell(0);
    var cell2 = newRow.insertCell(1);
    var cell3 = newRow.insertCell(2);
    var cell4 = newRow.insertCell(3);

    if (user.role == "client") {
        var cell5 = newRow.insertCell(4);
        cell5.setAttribute("type", "span")
        cell5.setAttribute("id", "deleteTable")
        cell5.innerHTML = "&times;";
        cell5.setAttribute("onclick", "deleteItem(" + i + ", " + e + ")")
        newRow.appendChild(cell5);
    }


    var checkInString = JSON.stringify(roomArray["room" + i][e].checkIn)
    checkInString = checkInString.replace("T00:00:00.000Z", "")
    var checkOutString = JSON.stringify(roomArray["room" + i][e].checkOut)
    checkOutString = checkOutString.replace("T00:00:00.000Z", "")

    cell1.innerHTML = roomArray["room" + i][e].nombre
    cell2.innerHTML = "room" + i
    cell3.innerHTML = checkInString
    cell4.innerHTML = checkOutString

    newRow.setAttribute("id", "table")
}

function deleteItem(i, e) {

    roomArray = JSON.parse(localStorage.getItem("lRoomsBookedArray"));

    delete roomArray["room" + i][e]

    localStorage.setItem("lRoomsBookedArray", JSON.stringify(roomArray));

    allReservations()
}

function food() {

    hideDivById("foodTable")

    var rowCount = document.getElementById("myFoodTable").rows.length;


    if (rowCount > 1) {

        deleteAllFoodTable(rowCount)
        insertTableFood()
    }
    else {
        insertTableFood()
    }
}





function insertTableFood() {

    foodArray = JSON.parse(localStorage.getItem("servicesBooked"));

    var loggedUser = JSON.parse(sessionStorage.getItem("loggedUser"));

    hideDivById("foodTable")

    var user = loadUserName()

    for (i = 0; i < foodArray.length; i++) {

        if (foodArray[i] != null) {

            if ((loggedUser.role == "client") && (user == foodArray[i].name)) {

                foodTable(foodArray, loggedUser, i)
            }
            else if (loggedUser.role == "admin") {
                foodTable(foodArray, loggedUser, i)
            }
        }
    }
}

function foodTable(foodArray, loggedUser, i) {
    var table = document.getElementById("myFoodTable");

    var newRow = table.insertRow(1);

    newRow.setAttribute("name", "reservation00")

    newRow.setAttribute("class", "active-row")

    var cell1 = newRow.insertCell(0);
    var cell2 = newRow.insertCell(1);
    var cell3 = newRow.insertCell(2);
    var cell4 = newRow.insertCell(3);

    if (loggedUser.role == "client") {
        cell4.setAttribute("type", "span")
        cell4.setAttribute("id", "deleteTable")
        cell4.innerHTML = "&times;";
        cell4.setAttribute("onclick", "deleteFoodItem( " + i + " )")
        newRow.appendChild(cell4);
    }

    cell1.innerHTML = foodArray[i].name
    cell2.innerHTML = foodArray[i].date
    cell3.innerHTML = foodArray[i].food
}

function deleteFoodItem(i) {

    foodArray = JSON.parse(localStorage.getItem("servicesBooked"));

    delete foodArray[i]

    localStorage.setItem("servicesBooked", JSON.stringify(foodArray));

    food()
}


w3.includeHTML()