





import java.util.List;
import java.util.ArrayList;

public class Post  {

    private String userName;
    private String Date;
    private String content;





    private User user;


    public Post(
        String userName,        String Date,        String content    ) {
        this.userName = userName;
        this.Date = Date;
        this.content = content;
    }


    public String getUsername() {
        return userName;
    }

    public void setUsername(String userName) {
        this.userName = userName;
    }
    public String getDate() {
        return Date;
    }

    public void setDate(String Date) {
        this.Date = Date;
    }
    public String getContent() {
        return content;
    }

    public void setContent(String content) {
        this.content = content;
    }

    public User getUser() {
        return user;
    }

    public void setUser(User user) {
        this.user = user;
    }

}