





import java.util.List;
import java.util.ArrayList;

public class Attachment  {

    private String User;
    private int AttachmentID;
    private String Path;
    private String Project;
    private String Extension;
    private String Name;
    private String Created;
    private String Size;



    public Attachment(
        String User,        int AttachmentID,        String Path,        String Project,        String Extension,        String Name,        String Created,        String Size    ) {
        this.User = User;
        this.AttachmentID = AttachmentID;
        this.Path = Path;
        this.Project = Project;
        this.Extension = Extension;
        this.Name = Name;
        this.Created = Created;
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
    public String getPath() {
        return Path;
    }

    public void setPath(String Path) {
        this.Path = Path;
    }
    public String getProject() {
        return Project;
    }

    public void setProject(String Project) {
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


}