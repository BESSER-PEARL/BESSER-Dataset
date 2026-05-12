





import java.util.List;
import java.util.ArrayList;

public class Attachment  {

    private String Path;
    private int AttachmentID;
    private None Project;
    private String Extension;
    private String Name;
    private None User;
    private String Size;
    private String Created;





    private User user;




    private Project project;


    public Attachment(
        String Path,        int AttachmentID,        None Project,        String Extension,        String Name,        None User,        String Size,        String Created    ) {
        this.Path = Path;
        this.AttachmentID = AttachmentID;
        this.Project = Project;
        this.Extension = Extension;
        this.Name = Name;
        this.User = User;
        this.Size = Size;
        this.Created = Created;
    }


    public String getPath() {
        return Path;
    }

    public void setPath(String Path) {
        this.Path = Path;
    }
    public int getAttachmentid() {
        return AttachmentID;
    }

    public void setAttachmentid(int AttachmentID) {
        this.AttachmentID = AttachmentID;
    }
    public None getProject() {
        return Project;
    }

    public void setProject(None Project) {
        this.Project = Project;
    }
    public String getExtension() {
        return Extension;
    }

    public void setExtension(String Extension) {
        this.Extension = Extension;
    }
    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }
    public None getUser() {
        return User;
    }

    public void setUser(None User) {
        this.User = User;
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