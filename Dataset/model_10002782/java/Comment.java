





import java.util.List;
import java.util.ArrayList;

public class Comment  {

    private String Content;
    private String Created;
    private None Project;
    private int CommentID;
    private None User;





    private Project project;




    private User user;


    public Comment(
        String Content,        String Created,        None Project,        int CommentID,        None User    ) {
        this.Content = Content;
        this.Created = Created;
        this.Project = Project;
        this.CommentID = CommentID;
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
    public None getUser() {
        return User;
    }

    public void setUser(None User) {
        this.User = User;
    }

    public Project getProject() {
        return project;
    }

    public void setProject(Project project) {
        this.project = project;
    }
    public User getUser() {
        return user;
    }

    public void setUser(User user) {
        this.user = user;
    }

}