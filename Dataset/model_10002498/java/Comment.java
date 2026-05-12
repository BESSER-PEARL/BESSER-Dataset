





import java.util.List;
import java.util.ArrayList;

public class Comment  {

    private int CommentID;
    private None User;
    private String Created;
    private None Project;
    private String Content;





    private User user;




    private Project project;


    public Comment(
        int CommentID,        None User,        String Created,        None Project,        String Content    ) {
        this.CommentID = CommentID;
        this.User = User;
        this.Created = Created;
        this.Project = Project;
        this.Content = Content;
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
    public String getContent() {
        return Content;
    }

    public void setContent(String Content) {
        this.Content = Content;
    }

    public User getUser() {
        return user;
    }

    public void setUser(User user) {
        this.user = user;
    }
    public Project getProject() {
        return project;
    }

    public void setProject(Project project) {
        this.project = project;
    }

}