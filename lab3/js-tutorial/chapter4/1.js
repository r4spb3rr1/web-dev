`Constructor for objects`

function User(name) {
  this.name = name;
  this.isAdmin = false;
}

let user = new User("Juzo");

alert(user.name)
