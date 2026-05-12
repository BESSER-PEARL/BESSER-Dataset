





import java.util.List;
import java.util.ArrayList;

public class Rol  {

    private String nombre;





    private List<User> users;


    public Rol(
        String nombre    ) {
        this.nombre = nombre;
        this.users = new ArrayList<>();
    }

    public Rol(
        String nombre        ArrayList<User> users    ) {
        this.nombre = nombre;
        this.users = users;
    }

    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public List<User> getUsers() {
        return users;
    }

    public void addUser(User user) {
        this.users.add(user);
    }

}