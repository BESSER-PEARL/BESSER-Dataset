





import java.util.List;
import java.util.ArrayList;

public class gametournament_Pool  {






    private List<gametournament_Gamer> gametournament_gamers;




    private gametournament_QualificationPhase gametournament_qualificationphase;




    private List<gametournament_Gamer> gametournament_gamers;


    public gametournament_Pool(
    ) {
        this.gametournament_gamers = new ArrayList<>();
        this.gametournament_gamers = new ArrayList<>();
    }

    public gametournament_Pool(
        ArrayList<gametournament_Gamer> gametournament_gamers,        ArrayList<gametournament_Gamer> gametournament_gamers    ) {
        this.gametournament_gamers = gametournament_gamers;
        this.gametournament_gamers = gametournament_gamers;
    }


    public List<gametournament_Gamer> getGametournament_gamers() {
        return gametournament_gamers;
    }

    public void addGametournament_gamer(Gametournament_gamer gametournament_gamer) {
        this.gametournament_gamers.add(gametournament_gamer);
    }
    public gametournament_QualificationPhase getGametournament_qualificationphase() {
        return gametournament_qualificationphase;
    }

    public void setGametournament_qualificationphase(gametournament_QualificationPhase gametournament_qualificationphase) {
        this.gametournament_qualificationphase = gametournament_qualificationphase;
    }
    public List<gametournament_Gamer> getGametournament_gamers() {
        return gametournament_gamers;
    }

    public void addGametournament_gamer(Gametournament_gamer gametournament_gamer) {
        this.gametournament_gamers.add(gametournament_gamer);
    }

}