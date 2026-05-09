





import java.util.List;
import java.util.ArrayList;

public class trackit_Issue extends Identifiable {

    private String title;
    private String dateCreated;
    private String description;
    private String issueType;
    private String status;





    private List<trackit_Issue> trackit_issues;




    private List<trackit_Issue> trackit_issues;




    private List<trackit_Version> trackit_versions;




    private List<trackit_Issue> trackit_issues;




    private List<trackit_Issue> trackit_issues;




    private trackit_IssueTracker trackit_issuetracker;




    private trackit_Version trackit_version;


    public trackit_Issue(
        String title,        String dateCreated,        String description,        String issueType,        String status    ) {
        super(
        );
        this.title = title;
        this.dateCreated = dateCreated;
        this.description = description;
        this.issueType = issueType;
        this.status = status;
        this.trackit_issues = new ArrayList<>();
        this.trackit_issues = new ArrayList<>();
        this.trackit_versions = new ArrayList<>();
        this.trackit_issues = new ArrayList<>();
        this.trackit_issues = new ArrayList<>();
    }

    public trackit_Issue(
        String title,        String dateCreated,        String description,        String issueType,        String status        ArrayList<trackit_Issue> trackit_issues,        ArrayList<trackit_Issue> trackit_issues,        ArrayList<trackit_Version> trackit_versions,        ArrayList<trackit_Issue> trackit_issues,        ArrayList<trackit_Issue> trackit_issues    ) {
        this.title = title;
        this.dateCreated = dateCreated;
        this.description = description;
        this.issueType = issueType;
        this.status = status;
        this.trackit_issues = trackit_issues;
        this.trackit_issues = trackit_issues;
        this.trackit_versions = trackit_versions;
        this.trackit_issues = trackit_issues;
        this.trackit_issues = trackit_issues;
    }

    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }
    public String getDatecreated() {
        return dateCreated;
    }

    public void setDatecreated(String dateCreated) {
        this.dateCreated = dateCreated;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public String getIssuetype() {
        return issueType;
    }

    public void setIssuetype(String issueType) {
        this.issueType = issueType;
    }
    public String getStatus() {
        return status;
    }

    public void setStatus(String status) {
        this.status = status;
    }

    public List<trackit_Issue> getTrackit_issues() {
        return trackit_issues;
    }

    public void addTrackit_issue(Trackit_issue trackit_issue) {
        this.trackit_issues.add(trackit_issue);
    }
    public List<trackit_Issue> getTrackit_issues() {
        return trackit_issues;
    }

    public void addTrackit_issue(Trackit_issue trackit_issue) {
        this.trackit_issues.add(trackit_issue);
    }
    public List<trackit_Version> getTrackit_versions() {
        return trackit_versions;
    }

    public void addTrackit_version(Trackit_version trackit_version) {
        this.trackit_versions.add(trackit_version);
    }
    public List<trackit_Issue> getTrackit_issues() {
        return trackit_issues;
    }

    public void addTrackit_issue(Trackit_issue trackit_issue) {
        this.trackit_issues.add(trackit_issue);
    }
    public List<trackit_Issue> getTrackit_issues() {
        return trackit_issues;
    }

    public void addTrackit_issue(Trackit_issue trackit_issue) {
        this.trackit_issues.add(trackit_issue);
    }
    public trackit_IssueTracker getTrackit_issuetracker() {
        return trackit_issuetracker;
    }

    public void setTrackit_issuetracker(trackit_IssueTracker trackit_issuetracker) {
        this.trackit_issuetracker = trackit_issuetracker;
    }
    public trackit_Version getTrackit_version() {
        return trackit_version;
    }

    public void setTrackit_version(trackit_Version trackit_version) {
        this.trackit_version = trackit_version;
    }

}