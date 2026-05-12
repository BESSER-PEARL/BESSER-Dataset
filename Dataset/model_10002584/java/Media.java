





import java.util.List;
import java.util.ArrayList;

public class Media  {

    private String MediaPath;





    private Post post;


    public Media(
        String MediaPath    ) {
        this.MediaPath = MediaPath;
    }


    public String getMediapath() {
        return MediaPath;
    }

    public void setMediapath(String MediaPath) {
        this.MediaPath = MediaPath;
    }

    public Post getPost() {
        return post;
    }

    public void setPost(Post post) {
        this.post = post;
    }

}