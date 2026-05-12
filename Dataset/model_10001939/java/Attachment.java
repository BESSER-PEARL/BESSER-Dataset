





import java.util.List;
import java.util.ArrayList;

public class Attachment  {

    private String Project;
    private String Path;
    private String Created;
    private String Size;
    private String User;
    private int AttachmentID;
    private String Name;
    private String Extension;



    public Attachment(
        String Project,        String Path,        String Created,        String Size,        String User,        int AttachmentID,        String Name,        String Extension    ) {
        this.Project = Project;
        this.Path = Path;
        this.Created = Created;
        this.Size = Size;
        this.User = User;
        this.AttachmentID = AttachmentID;
        this.Name = Name;
        this.Extension = Extension;
    }


    public String getProject() {
        return Project;
    }

    public void setProject(String Project) {
        this.Project = Project;
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
    public String getSize() {
        return Size;
    }

    public void setSize(String Size) {
        this.Size = Size;
    }
    public String getUser() {
        return User;
    }

    public void setUser(String User) {
        this.User = User;
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


}