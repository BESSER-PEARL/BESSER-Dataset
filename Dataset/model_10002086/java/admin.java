





import java.util.List;
import java.util.ArrayList;

public class admin  {

    private String password;
    private int id_admin;
    private String username;





    private List<testimoni> testimonis;




    private List<event> events;


    public admin(
        String password,        int id_admin,        String username    ) {
        this.password = password;
        this.id_admin = id_admin;
        this.username = username;
        this.testimonis = new ArrayList<>();
        this.events = new ArrayList<>();
    }

    public admin(
        String password,        int id_admin,        String username        ArrayList<testimoni> testimonis,        ArrayList<event> events    ) {
        this.password = password;
        this.id_admin = id_admin;
        this.username = username;
        this.testimonis = testimonis;
        this.events = events;
    }

    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }
    public int getId_admin() {
        return id_admin;
    }

    public void setId_admin(int id_admin) {
        this.id_admin = id_admin;
    }
    public String getUsername() {
        return username;
    }

    public void setUsername(String username) {
        this.username = username;
    }

    public List<testimoni> getTestimonis() {
        return testimonis;
    }

    public void addTestimoni(Testimoni testimoni) {
        this.testimonis.add(testimoni);
    }
    public List<event> getEvents() {
        return events;
    }

    public void addEvent(Event event) {
        this.events.add(event);
    }

}