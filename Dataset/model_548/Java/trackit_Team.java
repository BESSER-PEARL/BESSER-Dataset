





import java.util.List;
import java.util.ArrayList;

public class trackit_Team extends Identifiable {

    private String teamName;





    private trackit_IssueTracker trackit_issuetracker;


    public trackit_Team(
        String teamName    ) {
        super(
        );
        this.teamName = teamName;
    }


    public String getTeamname() {
        return teamName;
    }

    public void setTeamname(String teamName) {
        this.teamName = teamName;
    }

    public trackit_IssueTracker getTrackit_issuetracker() {
        return trackit_issuetracker;
    }

    public void setTrackit_issuetracker(trackit_IssueTracker trackit_issuetracker) {
        this.trackit_issuetracker = trackit_issuetracker;
    }

}