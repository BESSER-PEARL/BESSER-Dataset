





import java.util.List;
import java.util.ArrayList;

public class Comment  {

    private String Content;
    private None User;
    private String Created;
    private int CommentID;
    private None Project;





    private User user;




    private Project project;


    public Comment(
        String Content,        None User,        String Created,        int CommentID,        None Project    ) {
        this.Content = Content;
        this.User = User;
        this.Created = Created;
        this.CommentID = CommentID;
        this.Project = Project;
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