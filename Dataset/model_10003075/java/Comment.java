





import java.util.List;
import java.util.ArrayList;

public class Comment  {

    private String Created;
    private None Project;
    private String Content;
    private int CommentID;
    private None User;





    private Project project;




    private User user;


    public Comment(
        String Created,        None Project,        String Content,        int CommentID,        None User    ) {
        this.Created = Created;
        this.Project = Project;
        this.Content = Content;
        this.CommentID = CommentID;
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