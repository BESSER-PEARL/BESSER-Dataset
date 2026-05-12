





import java.util.List;
import java.util.ArrayList;

public class Comment  {

    private String Content;
    private String Created;
    private int CommentID;
    private String Project;
    private String User;



    public Comment(
        String Content,        String Created,        int CommentID,        String Project,        String User    ) {
        this.Content = Content;
        this.Created = Created;
        this.CommentID = CommentID;
        this.Project = Project;
        this.User = User;
    }


    public String getContent() {
        return Content;
    }

    public void setContent(String Content) {
        this.Content = Content;
    }
    public String getCreated() {
        return Created;
    }

    public void setCreated(String Created) {
        this.Created = Created;
    }
    public int getCommentid() {
        return CommentID;
    }

    public void setCommentid(int CommentID) {
        this.CommentID = CommentID;
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


}