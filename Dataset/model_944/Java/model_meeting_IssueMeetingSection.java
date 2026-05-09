





import java.util.List;
import java.util.ArrayList;

public class model_meeting_IssueMeetingSection extends MeetingSection {






    private List<rationale_Issue> rationale_issues;


    public model_meeting_IssueMeetingSection(
    ) {
        super(
        );
        this.rationale_issues = new ArrayList<>();
    }

    public model_meeting_IssueMeetingSection(
        ArrayList<rationale_Issue> rationale_issues    ) {
        this.rationale_issues = rationale_issues;
    }


    public List<rationale_Issue> getRationale_issues() {
        return rationale_issues;
    }

    public void addRationale_issue(Rationale_issue rationale_issue) {
        this.rationale_issues.add(rationale_issue);
    }

}