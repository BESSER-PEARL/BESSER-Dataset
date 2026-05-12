





import java.util.List;
import java.util.ArrayList;

public class Another_Login  {

    private int facebook_id;
    private int id;
    private int user_id;





    private Reciever reciever;


    public Another_Login(
        int facebook_id,        int id,        int user_id    ) {
        this.facebook_id = facebook_id;
        this.id = id;
        this.user_id = user_id;
    }


    public int getFacebook_id() {
        return facebook_id;
    }

    public void setFacebook_id(int facebook_id) {
        this.facebook_id = facebook_id;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
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

}