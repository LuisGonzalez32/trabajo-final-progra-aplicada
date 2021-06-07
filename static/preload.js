
function preLoadUsers() {

    var userArray = [{
        user: "luis",
        password: "123",
        role: "client"
    }, {
        user: "andres",
        password: "esquivel",
        role: "admin"
    }]

    localStorage.setItem("lUserArray", JSON.stringify(userArray))
}

function roomsBooked() {

    var roomsBookedArray = {
        room0: [],
        room1: [],
        room2: [],
        room3: [],
        room4: [],
        room5: []
    }

    localStorage.setItem("lRoomsBookedArray", JSON.stringify(roomsBookedArray))
}

function preLoadRooms() {

    var roomsArray = [{
        name: "room12",
        capacity: 3,
        balcon: "yes",
        price: 10
    },
    {
        name: "room23",
        capacity: 5,
        balcon: "yes",
        price: 20
    },
    {
        name: "room34",
        capacity: 5,
        balcon: "no",
        price: 25
    }, {
        name: "room45",
        capacity: 1,
        balcon: "yes",
        price: 10
    }, {
        name: "room56",
        capacity: 1,
        balcon: "no",
        price: 15
    }, {
        name: "room67",
        capacity: 3,
        balcon: "no",
        price: 25
    }]

    localStorage.setItem("lRoomsArray", JSON.stringify(roomsArray))
}

function services() {

    var servicesArray = [{
        food: "hamburguesa"
    },
    {
        food: "pizza"
    }]

    localStorage.setItem("services", JSON.stringify(servicesArray))
}

function servicesBooked() {

    var servicesBookedArray = []

    localStorage.setItem("servicesBooked", JSON.stringify(servicesBookedArray))
}

preLoadUsers()
preLoadRooms()
roomsBooked()
services()
servicesBooked()