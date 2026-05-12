





import java.util.List;
import java.util.ArrayList;

public class Panel  {

    private None Approval;
    private int Id;
    private int PreBufferTime;
    private int Length;
    private String Scheduled;
    private boolean Private;
    private String Description;
    private None Submitter;
    private None Resources;
    private None Panelists;
    private int PostBufferTime;
    private String Name;



    public Panel(
        None Approval,        int Id,        int PreBufferTime,        int Length,        String Scheduled,        boolean Private,        String Description,        None Submitter,        None Resources,        None Panelists,        int PostBufferTime,        String Name    ) {
        this.Approval = Approval;
        this.Id = Id;
        this.PreBufferTime = PreBufferTime;
        this.Length = Length;
        this.Scheduled = Scheduled;
        this.Private = Private;
        this.Description = Description;
        this.Submitter = Submitter;
        this.Resources = Resources;
        this.Panelists = Panelists;
        this.PostBufferTime = PostBufferTime;
        this.Name = Name;
    }


    public None getApproval() {
        return Approval;
    }

    public void setApproval(None Approval) {
        this.Approval = Approval;
    }
    public int getId() {
        return Id;
    }

    public void setId(int Id) {
        this.Id = Id;
    }
    public int getPrebuffertime() {
        return PreBufferTime;
    }

    public void setPrebuffertime(int PreBufferTime) {
        this.PreBufferTime = PreBufferTime;
    }
    public int getLength() {
        return Length;
    }

    public void setLength(int Length) {
        this.Length = Length;
    }
    public String getScheduled() {
        return Scheduled;
    }

    public void setScheduled(String Scheduled) {
        this.Scheduled = Scheduled;
    }
    public boolean getPrivate() {
        return Private;
    }

    public void setPrivate(boolean Private) {
        this.Private = Private;
    }
    public String getDescription() {
        return Description;
    }

    public void setDescription(String Description) {
        this.Description = Description;
    }
    public None getSubmitter() {
        return Submitter;
    }

    public void setSubmitter(None Submitter) {
        this.Submitter = Submitter;
    }
    public None getResources() {
        return Resources;
    }

    public void setResources(None Resources) {
        this.Resources = Resources;
    }
    public None getPanelists() {
        return Panelists;
    }

    public void setPanelists(None Panelists) {
        this.Panelists = Panelists;
    }
    public int getPostbuffertime() {
        return PostBufferTime;
    }

    public void setPostbuffertime(int PostBufferTime) {
        this.PostBufferTime = PostBufferTime;
    }
    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }


}