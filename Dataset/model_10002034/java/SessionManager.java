





import java.util.List;
import java.util.ArrayList;

public class SessionManager  {

    private int userID;
    private String categoryName;





    private User user;


    public SessionManager(
        int userID,        String categoryName    ) {
        this.userID = userID;
        this.categoryName = categoryName;
    }


    public int getUserid() {
        return userID;
    }

    public void setUserid(int userID) {
        this.userID = userID;
    }
    public String getCategoryname() {
        return categoryName;
    }

    public void setCategoryname(String categoryName) {
        this.categoryName = categoryName;
    }

    public User getUser() {
        return user;
    }

    public void setUser(User user) {
        this.user = user;
    }

}