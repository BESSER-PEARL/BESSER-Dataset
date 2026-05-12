





import java.util.List;
import java.util.ArrayList;

public class Comment  {

    private String CreationDate;
    private String Title;
    private String Body;
    private int Id;
    private None Creator;





    private User user;




    private Administrator administrator;


    public Comment(
        String CreationDate,        String Title,        String Body,        int Id,        None Creator    ) {
        this.CreationDate = CreationDate;
        this.Title = Title;
        this.Body = Body;
        this.Id = Id;
        this.Creator = Creator;
    }


    public String getCreationdate() {
        return CreationDate;
    }

    public void setCreationdate(String CreationDate) {
        this.CreationDate = CreationDate;
    }
    public String getTitle() {
        return Title;
    }

    public void setTitle(String Title) {
        this.Title = Title;
    }
    public String getBody() {
        return Body;
    }

    public void setBody(String Body) {
        this.Body = Body;
    }
    public int getId() {
        return Id;
    }

    public void setId(int Id) {
        this.Id = Id;
    }
    public None getCreator() {
        return Creator;
    }

    public void setCreator(None Creator) {
        this.Creator = Creator;
    }

    public User getUser() {
        return user;
    }

    public void setUser(User user) {
        this.user = user;
    }
    public Administrator getAdministrator() {
        return administrator;
    }

    public void setAdministrator(Administrator administrator) {
        this.administrator = administrator;
    }

}