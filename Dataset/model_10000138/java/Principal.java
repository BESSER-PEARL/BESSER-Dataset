





import java.util.List;
import java.util.ArrayList;

public class Principal  {

    private int id;
    private int followers_id;
    private String status;
    private String creation_date;
    private int user_id;





    private Reciever reciever;




    private List<Reciever> recievers;


    public Principal(
        int id,        int followers_id,        String status,        String creation_date,        int user_id    ) {
        this.id = id;
        this.followers_id = followers_id;
        this.status = status;
        this.creation_date = creation_date;
        this.user_id = user_id;
        this.recievers = new ArrayList<>();
    }

    public Principal(
        int id,        int followers_id,        String status,        String creation_date,        int user_id        ArrayList<Reciever> recievers    ) {
        this.id = id;
        this.followers_id = followers_id;
        this.status = status;
        this.creation_date = creation_date;
        this.user_id = user_id;
        this.recievers = recievers;
    }

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
    public int getFollowers_id() {
        return followers_id;
    }

    public void setFollowers_id(int followers_id) {
        this.followers_id = followers_id;
    }
    public String getStatus() {
        return status;
    }

    public void setStatus(String status) {
        this.status = status;
    }
    public String getCreation_date() {
        return creation_date;
    }

    public void setCreation_date(String creation_date) {
        this.creation_date = creation_date;
    }
    public int getUser_id() {
        return user_id;
    }

    public void setUser_id(int user_id) {
        this.user_id = user_id;
    }

    public Reciever getReciever() {
        return reciever;
    }

    public void setReciever(Reciever reciever) {
        this.reciever = reciever;
    }
    public List<Reciever> getRecievers() {
        return recievers;
    }

    public void addReciever(Reciever reciever) {
        this.recievers.add(reciever);
    }

}