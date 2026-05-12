





import java.util.List;
import java.util.ArrayList;

public class research_team_OpenPosition  {

    private String status;
    private String mission;
    private String duration;





    private research_team_Team research_team_team;


    public research_team_OpenPosition(
        String status,        String mission,        String duration    ) {
        this.status = status;
        this.mission = mission;
        this.duration = duration;
    }


    public String getStatus() {
        return status;
    }

    public void setStatus(String status) {
        this.status = status;
    }
    public String getMission() {
        return mission;
    }

    public void setMission(String mission) {
        this.mission = mission;
    }
    public String getDuration() {
        return duration;
    }

    public void setDuration(String duration) {
        this.duration = duration;
    }

    public research_team_Team getResearch_team_team() {
        return research_team_team;
    }

    public void setResearch_team_team(research_team_Team research_team_team) {
        this.research_team_team = research_team_team;
    }

}