





import java.util.List;
import java.util.ArrayList;

public class gametournament_FinalPhase  {






    private List<gametournament_Gamer> gametournament_gamers;




    private gametournament_Tournament gametournament_tournament;


    public gametournament_FinalPhase(
    ) {
        this.gametournament_gamers = new ArrayList<>();
    }

    public gametournament_FinalPhase(
        ArrayList<gametournament_Gamer> gametournament_gamers    ) {
        this.gametournament_gamers = gametournament_gamers;
    }


    public List<gametournament_Gamer> getGametournament_gamers() {
        return gametournament_gamers;
    }

    public void addGametournament_gamer(Gametournament_gamer gametournament_gamer) {
        this.gametournament_gamers.add(gametournament_gamer);
    }
    public gametournament_Tournament getGametournament_tournament() {
        return gametournament_tournament;
    }

    public void setGametournament_tournament(gametournament_Tournament gametournament_tournament) {
        this.gametournament_tournament = gametournament_tournament;
    }

}