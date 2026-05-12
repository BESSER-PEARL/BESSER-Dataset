





import java.util.List;
import java.util.ArrayList;

public class Following_Hashtag  {

    private int user_id;
    private int hashtag_id;
    private int id;





    private List<Reciever> recievers;




    private Hashtag hashtag;


    public Following_Hashtag(
        int user_id,        int hashtag_id,        int id    ) {
        this.user_id = user_id;
        this.hashtag_id = hashtag_id;
        this.id = id;
        this.recievers = new ArrayList<>();
    }

    public Following_Hashtag(
        int user_id,        int hashtag_id,        int id        ArrayList<Reciever> recievers    ) {
        this.user_id = user_id;
        this.hashtag_id = hashtag_id;
        this.id = id;
        this.recievers = recievers;
    }

    public int getUser_id() {
        return user_id;
    }

    public void setUser_id(int user_id) {
        this.user_id = user_id;
    }
    public int getHashtag_id() {
        return hashtag_id;
    }

    public void setHashtag_id(int hashtag_id) {
        this.hashtag_id = hashtag_id;
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
    public Hashtag getHashtag() {
        return hashtag;
    }

    public void setHashtag(Hashtag hashtag) {
        this.hashtag = hashtag;
    }

}