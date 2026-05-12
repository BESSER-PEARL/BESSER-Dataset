





import java.util.List;
import java.util.ArrayList;

public class Project  {

    private int StatusID;
    private String Activities___;
    private String Description;
    private String Attachments___;
    private None ProjectManager;
    private String Title;
    private int PriorityID;
    private int PorjectID;
    private None Author;
    private String Subscriptions___;
    private String Team___;
    private String Comments___;
    private None Assignee;
    private String Deadline;
    private String Created;





    private List<Attachment> attachments;




    private User user;




    private User user;




    private User user;




    private User user;




    private List<Comment> comments;


    public Project(
        int StatusID,        String Activities___,        String Description,        String Attachments___,        None ProjectManager,        String Title,        int PriorityID,        int PorjectID,        None Author,        String Subscriptions___,        String Team___,        String Comments___,        None Assignee,        String Deadline,        String Created    ) {
        this.StatusID = StatusID;
        this.Activities___ = Activities___;
        this.Description = Description;
        this.Attachments___ = Attachments___;
        this.ProjectManager = ProjectManager;
        this.Title = Title;
        this.PriorityID = PriorityID;
        this.PorjectID = PorjectID;
        this.Author = Author;
        this.Subscriptions___ = Subscriptions___;
        this.Team___ = Team___;
        this.Comments___ = Comments___;
        this.Assignee = Assignee;
        this.Deadline = Deadline;
        this.Created = Created;
        this.attachments = new ArrayList<>();
        this.comments = new ArrayList<>();
    }

    public Project(
        int StatusID,        String Activities___,        String Description,        String Attachments___,        None ProjectManager,        String Title,        int PriorityID,        int PorjectID,        None Author,        String Subscriptions___,        String Team___,        String Comments___,        None Assignee,        String Deadline,        String Created        ArrayList<Attachment> attachments,        ArrayList<Comment> comments    ) {
        this.StatusID = StatusID;
        this.Activities___ = Activities___;
        this.Description = Description;
        this.Attachments___ = Attachments___;
        this.ProjectManager = ProjectManager;
        this.Title = Title;
        this.PriorityID = PriorityID;
        this.PorjectID = PorjectID;
        this.Author = Author;
        this.Subscriptions___ = Subscriptions___;
        this.Team___ = Team___;
        this.Comments___ = Comments___;
        this.Assignee = Assignee;
        this.Deadline = Deadline;
        this.Created = Created;
        this.attachments = attachments;
        this.comments = comments;
    }

    public int getStatusid() {
        return StatusID;
    }

    public void setStatusid(int StatusID) {
        this.StatusID = StatusID;
    }
    public String getActivities___() {
        return Activities___;
    }

    public void setActivities___(String Activities___) {
        this.Activities___ = Activities___;
    }
    public String getDescription() {
        return Description;
    }

    public void setDescription(String Description) {
        this.Description = Description;
    }
    public String getAttachments___() {
        return Attachments___;
    }

    public void setAttachments___(String Attachments___) {
        this.Attachments___ = Attachments___;
    }
    public None getProjectmanager() {
        return ProjectManager;
    }

    public void setProjectmanager(None ProjectManager) {
        this.ProjectManager = ProjectManager;
    }
    public String getTitle() {
        return Title;
    }

    public void setTitle(String Title) {
        this.Title = Title;
    }
    public int getPriorityid() {
        return PriorityID;
    }

    public void setPriorityid(int PriorityID) {
        this.PriorityID = PriorityID;
    }
    public int getPorjectid() {
        return PorjectID;
    }

    public void setPorjectid(int PorjectID) {
        this.PorjectID = PorjectID;
    }
    public None getAuthor() {
        return Author;
    }

    public void setAuthor(None Author) {
        this.Author = Author;
    }
    public String getSubscriptions___() {
        return Subscriptions___;
    }

    public void setSubscriptions___(String Subscriptions___) {
        this.Subscriptions___ = Subscriptions___;
    }
    public String getTeam___() {
        return Team___;
    }

    public void setTeam___(String Team___) {
        this.Team___ = Team___;
    }
    public String getComments___() {
        return Comments___;
    }

    public void setComments___(String Comments___) {
        this.Comments___ = Comments___;
    }
    public None getAssignee() {
        return Assignee;
    }

    public void setAssignee(None Assignee) {
        this.Assignee = Assignee;
    }
    public String getDeadline() {
        return Deadline;
    }

    public void setDeadline(String Deadline) {
        this.Deadline = Deadline;
    }
    public String getCreated() {
        return Created;
    }

    public void setCreated(String Created) {
        this.Created = Created;
    }

    public List<Attachment> getAttachments() {
        return attachments;
    }

    public void addAttachment(Attachment attachment) {
        this.attachments.add(attachment);
    }
    public User getUser() {
        return user;
    }

    public void setUser(User user) {
        this.user = user;
    }
    public User getUser() {
        return user;
    }

    public void setUser(User user) {
        this.user = user;
    }
    public User getUser() {
        return user;
    }

    public void setUser(User user) {
        this.user = user;
    }
    public User getUser() {
        return user;
    }

    public void setUser(User user) {
        this.user = user;
    }
    public List<Comment> getComments() {
        return comments;
    }

    public void addComment(Comment comment) {
        this.comments.add(comment);
    }

}