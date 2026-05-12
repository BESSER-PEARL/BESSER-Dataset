





import java.util.List;
import java.util.ArrayList;

public class Post  {

    private String creation_date;
    private String status;
    private int total_like;
    private int location_id;
    private String text;
    private int id;
    private String date_update;
    private int hashtag_id;





    private Reciever reciever;


    public Post(
        String creation_date,        String status,        int total_like,        int location_id,        String text,        int id,        String date_update,        int hashtag_id    ) {
        this.creation_date = creation_date;
        this.status = status;
        this.total_like = total_like;
        this.location_id = location_id;
        this.text = text;
        this.id = id;
        this.date_update = date_update;
        this.hashtag_id = hashtag_id;
    }


    public String getCreation_date() {
        return creation_date;
    }

    public void setCreation_date(String creation_date) {
        this.creation_date = creation_date;
    }
    public String getStatus() {
        return status;
    }

    public void setStatus(String status) {
        this.status = status;
    }
    public int getTotal_like() {
        return total_like;
    }

    public void setTotal_like(int total_like) {
        this.total_like = total_like;
    }
    public int getLocation_id() {
        return location_id;
    }

    public void setLocation_id(int location_id) {
        this.location_id = location_id;
    }
    public String getText() {
        return text;
    }

    public void setText(String text) {
        this.text = text;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
    public String getDate_update() {
        return date_update;
    }

    public void setDate_update(String date_update) {
        this.date_update = date_update;
    }
    public int getHashtag_id() {
        return hashtag_id;
    }

    public void setHashtag_id(int hashtag_id) {
        this.hashtag_id = hashtag_id;
    }

    public Reciever getReciever() {
        return reciever;
    }

    public void setReciever(Reciever reciever) {
        this.reciever = reciever;
    }

}