





import java.util.List;
import java.util.ArrayList;

public class Comment  {

    private int CommentID;
    private String Created;
    private String Project;
    private String User;
    private String Content;



    public Comment(
        int CommentID,        String Created,        String Project,        String User,        String Content    ) {
        this.CommentID = CommentID;
        this.Created = Created;
        this.Project = Project;
        this.User = User;
        this.Content = Content;
    }


    public int getCommentid() {
        return CommentID;
    }

    public void setCommentid(int CommentID) {
        this.CommentID = CommentID;
    }
    public String getCreated() {
        return Created;
    }

    public void setCreated(String Created) {
        this.Created = Created;
    }
    public String getProject() {
        return Project;
    }

    public void setProject(String Project) {
        this.Project = Project;
    }
    public String getUser() {
        return User;
    }

    public void setUser(String User) {
        this.User = User;
    }
    public String getContent() {
        return Content;
    }

    public void setContent(String Content) {
        this.Content = Content;
    }


}