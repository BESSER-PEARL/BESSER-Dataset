





import java.util.List;
import java.util.ArrayList;

public class Attachment  {

    private String Size;
    private String Name;
    private String Created;
    private String Path;
    private String Extension;
    private None Project;
    private None User;
    private int AttachmentID;





    private User user;




    private Project project;


    public Attachment(
        String Size,        String Name,        String Created,        String Path,        String Extension,        None Project,        None User,        int AttachmentID    ) {
        this.Size = Size;
        this.Name = Name;
        this.Created = Created;
        this.Path = Path;
        this.Extension = Extension;
        this.Project = Project;
        this.User = User;
        this.AttachmentID = AttachmentID;
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
    public String getCreated() {
        return Created;
    }

    public void setCreated(String Created) {
        this.Created = Created;
    }
    public String getPath() {
        return Path;
    }

    public void setPath(String Path) {
        this.Path = Path;
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
    public None getUser() {
        return User;
    }

    public void setUser(None User) {
        this.User = User;
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