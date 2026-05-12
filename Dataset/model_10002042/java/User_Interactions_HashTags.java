





import java.util.List;
import java.util.ArrayList;

public class User_Interactions_HashTags  {

    private String allHashTags;





    private User_Interactions_Post user_interactions_post;


    public User_Interactions_HashTags(
        String allHashTags    ) {
        this.allHashTags = allHashTags;
    }


    public String getAllhashtags() {
        return allHashTags;
    }

    public void setAllhashtags(String allHashTags) {
        this.allHashTags = allHashTags;
    }

    public User_Interactions_Post getUser_interactions_post() {
        return user_interactions_post;
    }

    public void setUser_interactions_post(User_Interactions_Post user_interactions_post) {
        this.user_interactions_post = user_interactions_post;
    }

}