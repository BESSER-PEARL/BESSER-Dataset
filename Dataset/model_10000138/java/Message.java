





import java.util.List;
import java.util.ArrayList;

public class Message  {

    private String date_seen;
    private String message;
    private int sender_id;
    private String creation_date;
    private boolean is_deleted;
    private int receiver_id;
    private int id;





    private List<Reciever> recievers;


    public Message(
        String date_seen,        String message,        int sender_id,        String creation_date,        boolean is_deleted,        int receiver_id,        int id    ) {
        this.date_seen = date_seen;
        this.message = message;
        this.sender_id = sender_id;
        this.creation_date = creation_date;
        this.is_deleted = is_deleted;
        this.receiver_id = receiver_id;
        this.id = id;
        this.recievers = new ArrayList<>();
    }

    public Message(
        String date_seen,        String message,        int sender_id,        String creation_date,        boolean is_deleted,        int receiver_id,        int id        ArrayList<Reciever> recievers    ) {
        this.date_seen = date_seen;
        this.message = message;
        this.sender_id = sender_id;
        this.creation_date = creation_date;
        this.is_deleted = is_deleted;
        this.receiver_id = receiver_id;
        this.id = id;
        this.recievers = recievers;
    }

    public String getDate_seen() {
        return date_seen;
    }

    public void setDate_seen(String date_seen) {
        this.date_seen = date_seen;
    }
    public String getMessage() {
        return message;
    }

    public void setMessage(String message) {
        this.message = message;
    }
    public int getSender_id() {
        return sender_id;
    }

    public void setSender_id(int sender_id) {
        this.sender_id = sender_id;
    }
    public String getCreation_date() {
        return creation_date;
    }

    public void setCreation_date(String creation_date) {
        this.creation_date = creation_date;
    }
    public boolean getIs_deleted() {
        return is_deleted;
    }

    public void setIs_deleted(boolean is_deleted) {
        this.is_deleted = is_deleted;
    }
    public int getReceiver_id() {
        return receiver_id;
    }

    public void setReceiver_id(int receiver_id) {
        this.receiver_id = receiver_id;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public List<Reciever> getRecievers() {
        return recievers;
    }

    public void addReciever(Reciever reciever) {
        this.recievers.add(reciever);
    }

}