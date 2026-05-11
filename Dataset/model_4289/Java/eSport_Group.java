





import java.util.List;
import java.util.ArrayList;

public class eSport_Group  {






    private eSport_GroupStage esport_groupstage;




    private List<eSport_Team> esport_teams;




    private eSport_Match esport_match;




    private eSport_Team esport_team;




    private List<eSport_Match> esport_matchs;




    private eSport_GroupStage esport_groupstage;


    public eSport_Group(
    ) {
        this.esport_teams = new ArrayList<>();
        this.esport_matchs = new ArrayList<>();
    }

    public eSport_Group(
        ArrayList<eSport_Team> esport_teams,        ArrayList<eSport_Match> esport_matchs    ) {
        this.esport_teams = esport_teams;
        this.esport_matchs = esport_matchs;
    }


    public eSport_GroupStage getEsport_groupstage() {
        return esport_groupstage;
    }

    public void setEsport_groupstage(eSport_GroupStage esport_groupstage) {
        this.esport_groupstage = esport_groupstage;
    }
    public List<eSport_Team> getEsport_teams() {
        return esport_teams;
    }

    public void addEsport_team(Esport_team esport_team) {
        this.esport_teams.add(esport_team);
    }
    public eSport_Match getEsport_match() {
        return esport_match;
    }

    public void setEsport_match(eSport_Match esport_match) {
        this.esport_match = esport_match;
    }
    public eSport_Team getEsport_team() {
        return esport_team;
    }

    public void setEsport_team(eSport_Team esport_team) {
        this.esport_team = esport_team;
    }
    public List<eSport_Match> getEsport_matchs() {
        return esport_matchs;
    }

    public void addEsport_match(Esport_match esport_match) {
        this.esport_matchs.add(esport_match);
    }
    public eSport_GroupStage getEsport_groupstage() {
        return esport_groupstage;
    }

    public void setEsport_groupstage(eSport_GroupStage esport_groupstage) {
        this.esport_groupstage = esport_groupstage;
    }

}