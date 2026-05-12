





import java.util.List;
import java.util.ArrayList;

public class Comment  {






    private Topic topic;




    private User user;


    public Comment(
    ) {
    }



    public Topic getTopic() {
        return topic;
    }

    public void setTopic(Topic topic) {
        this.topic = topic;
    }
    public User getUser() {
        return user;
    }

    public void setUser(User user) {
        this.user = user;
    }

}