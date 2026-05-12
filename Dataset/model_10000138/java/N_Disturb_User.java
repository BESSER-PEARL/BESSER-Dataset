





import java.util.List;
import java.util.ArrayList;

public class N_Disturb_User  {

    private int disturb_user_id;
    private int user_id;
    private int id;





    private Reciever reciever;


    public N_Disturb_User(
        int disturb_user_id,        int user_id,        int id    ) {
        this.disturb_user_id = disturb_user_id;
        this.user_id = user_id;
        this.id = id;
    }


    public int getDisturb_user_id() {
        return disturb_user_id;
    }

    public void setDisturb_user_id(int disturb_user_id) {
        this.disturb_user_id = disturb_user_id;
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

    public Reciever getReciever() {
        return reciever;
    }

    public void setReciever(Reciever reciever) {
        this.reciever = reciever;
    }

}