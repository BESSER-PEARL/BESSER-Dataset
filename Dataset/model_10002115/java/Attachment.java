





import java.util.List;
import java.util.ArrayList;

public class Attachment  {

    private None User;
    private String Path;
    private String Size;
    private String Created;
    private None Project;
    private int AttachmentID;
    private String Name;
    private String Extension;





    private User user;




    private Project project;


    public Attachment(
        None User,        String Path,        String Size,        String Created,        None Project,        int AttachmentID,        String Name,        String Extension    ) {
        this.User = User;
        this.Path = Path;
        this.Size = Size;
        this.Created = Created;
        this.Project = Project;
        this.AttachmentID = AttachmentID;
        this.Name = Name;
        this.Extension = Extension;
    }


    public None getUser() {
        return User;
    }

    public void setUser(None User) {
        this.User = User;
    }
    public String getPath() {
        return Path;
    }

    public void setPath(String Path) {
        this.Path = Path;
    }
    public String getSize() {
        return Size;
    }

    public void setSize(String Size) {
        this.Size = Size;
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
    public int getAttachmentid() {
        return AttachmentID;
    }

    public void setAttachmentid(int AttachmentID) {
        this.AttachmentID = AttachmentID;
    }
    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }
    public String getExtension() {
        return Extension;
    }

    public void setExtension(String Extension) {
        this.Extension = Extension;
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