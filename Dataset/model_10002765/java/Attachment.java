





import java.util.List;
import java.util.ArrayList;

public class Attachment  {

    private String Size;
    private None Project;
    private String Extension;
    private int AttachmentID;
    private None User;
    private String Created;
    private String Path;
    private String Name;



    public Attachment(
        String Size,        None Project,        String Extension,        int AttachmentID,        None User,        String Created,        String Path,        String Name    ) {
        this.Size = Size;
        this.Project = Project;
        this.Extension = Extension;
        this.AttachmentID = AttachmentID;
        this.User = User;
        this.Created = Created;
        this.Path = Path;
        this.Name = Name;
    }


    public String getSize() {
        return Size;
    }

    public void setSize(String Size) {
        this.Size = Size;
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
    public int getAttachmentid() {
        return AttachmentID;
    }

    public void setAttachmentid(int AttachmentID) {
        this.AttachmentID = AttachmentID;
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
    public String getPath() {
        return Path;
    }

    public void setPath(String Path) {
        this.Path = Path;
    }
    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }


}