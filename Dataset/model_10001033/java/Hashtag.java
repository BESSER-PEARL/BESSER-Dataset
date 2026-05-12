





import java.util.List;
import java.util.ArrayList;

public class Hashtag  {

    private String name;
    private int numOfRepeat;





    private User user;


    public Hashtag(
        String name,        int numOfRepeat    ) {
        this.name = name;
        this.numOfRepeat = numOfRepeat;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public int getNumofrepeat() {
        return numOfRepeat;
    }

    public void setNumofrepeat(int numOfRepeat) {
        this.numOfRepeat = numOfRepeat;
    }

    public User getUser() {
        return user;
    }

    public void setUser(User user) {
        this.user = user;
    }

}