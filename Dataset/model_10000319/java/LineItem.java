





import java.util.List;
import java.util.ArrayList;

public class LineItem  {

    private float tags;
    private int category;





    private AddPost addpost;




    private Post post;


    public LineItem(
        float tags,        int category    ) {
        this.tags = tags;
        this.category = category;
    }


    public float getTags() {
        return tags;
    }

    public void setTags(float tags) {
        this.tags = tags;
    }
    public int getCategory() {
        return category;
    }

    public void setCategory(int category) {
        this.category = category;
    }

    public AddPost getAddpost() {
        return addpost;
    }

    public void setAddpost(AddPost addpost) {
        this.addpost = addpost;
    }
    public Post getPost() {
        return post;
    }

    public void setPost(Post post) {
        this.post = post;
    }

}