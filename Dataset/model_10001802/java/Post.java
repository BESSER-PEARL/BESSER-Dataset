





import java.util.List;
import java.util.ArrayList;

public class Post  {

    private String privacy;
    private String info;
    private int price;





    private User user;


    public Post(
        String privacy,        String info,        int price    ) {
        this.privacy = privacy;
        this.info = info;
        this.price = price;
    }


    public String getPrivacy() {
        return privacy;
    }

    public void setPrivacy(String privacy) {
        this.privacy = privacy;
    }
    public String getInfo() {
        return info;
    }

    public void setInfo(String info) {
        this.info = info;
    }
    public int getPrice() {
        return price;
    }

    public void setPrice(int price) {
        this.price = price;
    }

    public User getUser() {
        return user;
    }

    public void setUser(User user) {
        this.user = user;
    }

}