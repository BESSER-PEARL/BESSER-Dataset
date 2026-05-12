





import java.util.List;
import java.util.ArrayList;

public class Cryptostream  {

    private int id;
    private int blocked_user_id;
    private int user_id;





    private Reciever reciever;


    public Cryptostream(
        int id,        int blocked_user_id,        int user_id    ) {
        this.id = id;
        this.blocked_user_id = blocked_user_id;
        this.user_id = user_id;
    }


    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
    public int getBlocked_user_id() {
        return blocked_user_id;
    }

    public void setBlocked_user_id(int blocked_user_id) {
        this.blocked_user_id = blocked_user_id;
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