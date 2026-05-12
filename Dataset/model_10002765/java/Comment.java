





import java.util.List;
import java.util.ArrayList;

public class Comment  {

    private None Project;
    private int CommentID;
    private String Content;
    private None User;
    private String Created;



    public Comment(
        None Project,        int CommentID,        String Content,        None User,        String Created    ) {
        this.Project = Project;
        this.CommentID = CommentID;
        this.Content = Content;
        this.User = User;
        this.Created = Created;
    }


    public None getProject() {
        return Project;
    }

    public void setProject(None Project) {
        this.Project = Project;
    }
    public int getCommentid() {
        return CommentID;
    }

    public void setCommentid(int CommentID) {
        this.CommentID = CommentID;
    }
    public String getContent() {
        return Content;
    }

    public void setContent(String Content) {
        this.Content = Content;
    }
    public None getUser() {
        return User;
    }

    public void setUser(None User) {
        this.User = User;
    }
    public String getCreated() {
        return Created;
    }

    public void setCreated(String Created) {
        this.Created = Created;
    }


}