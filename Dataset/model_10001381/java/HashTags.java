





import java.util.List;
import java.util.ArrayList;

public class HashTags  {

    private String allHashTags;





    private Post post;


    public HashTags(
        String allHashTags    ) {
        this.allHashTags = allHashTags;
    }


    public String getAllhashtags() {
        return allHashTags;
    }

    public void setAllhashtags(String allHashTags) {
        this.allHashTags = allHashTags;
    }

    public Post getPost() {
        return post;
    }

    public void setPost(Post post) {
        this.post = post;
    }

}