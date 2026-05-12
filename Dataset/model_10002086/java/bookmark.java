





import java.util.List;
import java.util.ArrayList;

public class bookmark  {

    private int id_user;
    private int id_event;
    private int id_bookmark;





    private user user;


    public bookmark(
        int id_user,        int id_event,        int id_bookmark    ) {
        this.id_user = id_user;
        this.id_event = id_event;
        this.id_bookmark = id_bookmark;
    }


    public int getId_user() {
        return id_user;
    }

    public void setId_user(int id_user) {
        this.id_user = id_user;
    }
    public int getId_event() {
        return id_event;
    }

    public void setId_event(int id_event) {
        this.id_event = id_event;
    }
    public int getId_bookmark() {
        return id_bookmark;
    }

    public void setId_bookmark(int id_bookmark) {
        this.id_bookmark = id_bookmark;
    }

    public user getUser() {
        return user;
    }

    public void setUser(user user) {
        this.user = user;
    }

}