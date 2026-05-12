





import java.util.List;
import java.util.ArrayList;

public class bean_FriendRequest  {

    private None date;
    private String email1;
    private int id;
    private String email2;



    public bean_FriendRequest(
        None date,        String email1,        int id,        String email2    ) {
        this.date = date;
        this.email1 = email1;
        this.id = id;
        this.email2 = email2;
    }


    public None getDate() {
        return date;
    }

    public void setDate(None date) {
        this.date = date;
    }
    public String getEmail1() {
        return email1;
    }

    public void setEmail1(String email1) {
        this.email1 = email1;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
    public String getEmail2() {
        return email2;
    }

    public void setEmail2(String email2) {
        this.email2 = email2;
    }


}