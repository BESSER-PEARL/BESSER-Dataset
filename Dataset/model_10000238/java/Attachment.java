





import java.util.List;
import java.util.ArrayList;

public class Attachment  {

    private None User;
    private String Extension;
    private None Project;
    private String Size;
    private String Path;
    private String Created;
    private String Name;
    private int AttachmentID;





    private Project project;




    private User user;


    public Attachment(
        None User,        String Extension,        None Project,        String Size,        String Path,        String Created,        String Name,        int AttachmentID    ) {
        this.User = User;
        this.Extension = Extension;
        this.Project = Project;
        this.Size = Size;
        this.Path = Path;
        this.Created = Created;
        this.Name = Name;
        this.AttachmentID = AttachmentID;
    }


    public None getUser() {
        return User;
    }

    public void setUser(None User) {
        this.User = User;
    }
    public String getExtension() {
        return Extension;
    }

    public void setExtension(String Extension) {
        this.Extension = Extension;
    }
    public None getProject() {
        return Project;
    }

    public void setProject(None Project) {
        this.Project = Project;
    }
    public String getSize() {
        return Size;
    }

    public void setSize(String Size) {
        this.Size = Size;
    }
    public String getPath() {
        return Path;
    }

    public void setPath(String Path) {
        this.Path = Path;
    }
    public String getCreated() {
        return Created;
    }

    public void setCreated(String Created) {
        this.Created = Created;
    }
    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }
    public int getAttachmentid() {
        return AttachmentID;
    }

    public void setAttachmentid(int AttachmentID) {
        this.AttachmentID = AttachmentID;
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