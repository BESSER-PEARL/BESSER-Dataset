





import java.util.List;
import java.util.ArrayList;

public class Sender  {

    private String status;
    private int user_id;
    private int id;
    private String creation_date;
    private int following_id;





    private List<Reciever> recievers;


    public Sender(
        String status,        int user_id,        int id,        String creation_date,        int following_id    ) {
        this.status = status;
        this.user_id = user_id;
        this.id = id;
        this.creation_date = creation_date;
        this.following_id = following_id;
        this.recievers = new ArrayList<>();
    }

    public Sender(
        String status,        int user_id,        int id,        String creation_date,        int following_id        ArrayList<Reciever> recievers    ) {
        this.status = status;
        this.user_id = user_id;
        this.id = id;
        this.creation_date = creation_date;
        this.following_id = following_id;
        this.recievers = recievers;
    }

    public String getStatus() {
        return status;
    }

    public void setStatus(String status) {
        this.status = status;
    }
    public int getUser_id() {
        return user_id;
    }

    public void setUser_id(int user_id) {
        this.user_id = user_id;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
    public String getCreation_date() {
        return creation_date;
    }

    public void setCreation_date(String creation_date) {
        this.creation_date = creation_date;
    }
    public int getFollowing_id() {
        return following_id;
    }

    public void setFollowing_id(int following_id) {
        this.following_id = following_id;
    }

    public List<Reciever> getRecievers() {
        return recievers;
    }

    public void addReciever(Reciever reciever) {
        this.recievers.add(reciever);
    }

}