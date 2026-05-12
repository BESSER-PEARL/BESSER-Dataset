





import java.util.List;
import java.util.ArrayList;

public class Comment  {

    private String Content;
    private None User;
    private None Project;
    private int CommentID;
    private String Created;





    private Project project;




    private User user;


    public Comment(
        String Content,        None User,        None Project,        int CommentID,        String Created    ) {
        this.Content = Content;
        this.User = User;
        this.Project = Project;
        this.CommentID = CommentID;
        this.Created = Created;
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
    public String getCreated() {
        return Created;
    }

    public void setCreated(String Created) {
        this.Created = Created;
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