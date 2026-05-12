





import java.util.List;
import java.util.ArrayList;

public class bean_TableBean  {

    private String displayed;
    private int postId;
    private String friendEmail;



    public bean_TableBean(
        String displayed,        int postId,        String friendEmail    ) {
        this.displayed = displayed;
        this.postId = postId;
        this.friendEmail = friendEmail;
    }


    public String getDisplayed() {
        return displayed;
    }

    public void setDisplayed(String displayed) {
        this.displayed = displayed;
    }
    public int getPostid() {
        return postId;
    }

    public void setPostid(int postId) {
        this.postId = postId;
    }
    public String getFriendemail() {
        return friendEmail;
    }

    public void setFriendemail(String friendEmail) {
        this.friendEmail = friendEmail;
    }


}