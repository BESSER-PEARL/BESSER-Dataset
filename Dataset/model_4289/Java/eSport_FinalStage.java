





import java.util.List;
import java.util.ArrayList;

public class eSport_FinalStage  {

    private int maxNbGames;





    private eSport_Tournament esport_tournament;




    private eSport_Tournament esport_tournament;




    private List<eSport_Team> esport_teams;




    private eSport_Team esport_team;


    public eSport_FinalStage(
        int maxNbGames    ) {
        this.maxNbGames = maxNbGames;
        this.esport_teams = new ArrayList<>();
    }

    public eSport_FinalStage(
        int maxNbGames        ArrayList<eSport_Team> esport_teams    ) {
        this.maxNbGames = maxNbGames;
        this.esport_teams = esport_teams;
    }

    public int getMaxnbgames() {
        return maxNbGames;
    }

    public void setMaxnbgames(int maxNbGames) {
        this.maxNbGames = maxNbGames;
    }

    public eSport_Tournament getEsport_tournament() {
        return esport_tournament;
    }

    public void setEsport_tournament(eSport_Tournament esport_tournament) {
        this.esport_tournament = esport_tournament;
    }
    public eSport_Tournament getEsport_tournament() {
        return esport_tournament;
    }

    public void setEsport_tournament(eSport_Tournament esport_tournament) {
        this.esport_tournament = esport_tournament;
    }
    public List<eSport_Team> getEsport_teams() {
        return esport_teams;
    }

    public void addEsport_team(Esport_team esport_team) {
        this.esport_teams.add(esport_team);
    }
    public eSport_Team getEsport_team() {
        return esport_team;
    }

    public void setEsport_team(eSport_Team esport_team) {
        this.esport_team = esport_team;
    }

}