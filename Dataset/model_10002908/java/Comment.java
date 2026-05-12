





import java.util.List;
import java.util.ArrayList;

public class Comment  {

    private None User;
    private String Content;
    private int CommentID;
    private None Project;
    private String Created;





    private Project project;




    private User user;


    public Comment(
        None User,        String Content,        int CommentID,        None Project,        String Created    ) {
        this.User = User;
        this.Content = Content;
        this.CommentID = CommentID;
        this.Project = Project;
        this.Created = Created;
    }


    public None getUser() {
        return User;
    }

    public void setUser(None User) {
        this.User = User;
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
    public None getProject() {
        return Project;
    }

    public void setProject(None Project) {
        this.Project = Project;
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