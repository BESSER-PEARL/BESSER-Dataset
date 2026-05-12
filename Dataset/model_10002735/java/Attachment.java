





import java.util.List;
import java.util.ArrayList;

public class Attachment  {

    private None User;
    private String Extension;
    private String Size;
    private String Name;
    private String Path;
    private None Project;
    private String Created;
    private int AttachmentID;





    private User user;




    private Project project;


    public Attachment(
        None User,        String Extension,        String Size,        String Name,        String Path,        None Project,        String Created,        int AttachmentID    ) {
        this.User = User;
        this.Extension = Extension;
        this.Size = Size;
        this.Name = Name;
        this.Path = Path;
        this.Project = Project;
        this.Created = Created;
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
    public String getSize() {
        return Size;
    }

    public void setSize(String Size) {
        this.Size = Size;
    }
    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }
    public String getPath() {
        return Path;
    }

    public void setPath(String Path) {
        this.Path = Path;
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
    public int getAttachmentid() {
        return AttachmentID;
    }

    public void setAttachmentid(int AttachmentID) {
        this.AttachmentID = AttachmentID;
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