





import java.util.List;
import java.util.ArrayList;

public class research_team_Collaboration  {

    private String status;
    private String title;
    private String from_;
    private String until;
    private String website;





    private research_team_Person research_team_person;




    private research_team_OpenPosition research_team_openposition;




    private research_team_Team research_team_team;


    public research_team_Collaboration(
        String status,        String title,        String from_,        String until,        String website    ) {
        this.status = status;
        this.title = title;
        this.from_ = from_;
        this.until = until;
        this.website = website;
    }


    public String getStatus() {
        return status;
    }

    public void setStatus(String status) {
        this.status = status;
    }
    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }
    public String getFrom_() {
        return from_;
    }

    public void setFrom_(String from_) {
        this.from_ = from_;
    }
    public String getUntil() {
        return until;
    }

    public void setUntil(String until) {
        this.until = until;
    }
    public String getWebsite() {
        return website;
    }

    public void setWebsite(String website) {
        this.website = website;
    }

    public research_team_Person getResearch_team_person() {
        return research_team_person;
    }

    public void setResearch_team_person(research_team_Person research_team_person) {
        this.research_team_person = research_team_person;
    }
    public research_team_OpenPosition getResearch_team_openposition() {
        return research_team_openposition;
    }

    public void setResearch_team_openposition(research_team_OpenPosition research_team_openposition) {
        this.research_team_openposition = research_team_openposition;
    }
    public research_team_Team getResearch_team_team() {
        return research_team_team;
    }

    public void setResearch_team_team(research_team_Team research_team_team) {
        this.research_team_team = research_team_team;
    }

}