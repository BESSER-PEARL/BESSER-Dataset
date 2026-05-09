





import java.util.List;
import java.util.ArrayList;

public class trackit_Member extends Identifiable {

    private String firstName;
    private String lastName;
    private String fullName;





    private trackit_Issue trackit_issue;




    private trackit_Issue trackit_issue;




    private trackit_Team trackit_team;




    private trackit_IssueTracker trackit_issuetracker;




    private List<trackit_Issue> trackit_issues;




    private List<trackit_Issue> trackit_issues;


    public trackit_Member(
        String firstName,        String lastName,        String fullName    ) {
        super(
        );
        this.firstName = firstName;
        this.lastName = lastName;
        this.fullName = fullName;
        this.trackit_issues = new ArrayList<>();
        this.trackit_issues = new ArrayList<>();
    }

    public trackit_Member(
        String firstName,        String lastName,        String fullName        ArrayList<trackit_Issue> trackit_issues,        ArrayList<trackit_Issue> trackit_issues    ) {
        this.firstName = firstName;
        this.lastName = lastName;
        this.fullName = fullName;
        this.trackit_issues = trackit_issues;
        this.trackit_issues = trackit_issues;
    }

    public String getFirstname() {
        return firstName;
    }

    public void setFirstname(String firstName) {
        this.firstName = firstName;
    }
    public String getLastname() {
        return lastName;
    }

    public void setLastname(String lastName) {
        this.lastName = lastName;
    }
    public String getFullname() {
        return fullName;
    }

    public void setFullname(String fullName) {
        this.fullName = fullName;
    }

    public trackit_Issue getTrackit_issue() {
        return trackit_issue;
    }

    public void setTrackit_issue(trackit_Issue trackit_issue) {
        this.trackit_issue = trackit_issue;
    }
    public trackit_Issue getTrackit_issue() {
        return trackit_issue;
    }

    public void setTrackit_issue(trackit_Issue trackit_issue) {
        this.trackit_issue = trackit_issue;
    }
    public trackit_Team getTrackit_team() {
        return trackit_team;
    }

    public void setTrackit_team(trackit_Team trackit_team) {
        this.trackit_team = trackit_team;
    }
    public trackit_IssueTracker getTrackit_issuetracker() {
        return trackit_issuetracker;
    }

    public void setTrackit_issuetracker(trackit_IssueTracker trackit_issuetracker) {
        this.trackit_issuetracker = trackit_issuetracker;
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

}