





import java.util.List;
import java.util.ArrayList;

public class eSport_Team  {

    private int championshipPoints;
    private String name;





    private eSport_Coach esport_coach;




    private eSport_Coach esport_coach;




    private eSport_Player esport_player;




    private List<eSport_Player> esport_players;


    public eSport_Team(
        int championshipPoints,        String name    ) {
        this.championshipPoints = championshipPoints;
        this.name = name;
        this.esport_players = new ArrayList<>();
    }

    public eSport_Team(
        int championshipPoints,        String name        ArrayList<eSport_Player> esport_players    ) {
        this.championshipPoints = championshipPoints;
        this.name = name;
        this.esport_players = esport_players;
    }

    public int getChampionshippoints() {
        return championshipPoints;
    }

    public void setChampionshippoints(int championshipPoints) {
        this.championshipPoints = championshipPoints;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public eSport_Coach getEsport_coach() {
        return esport_coach;
    }

    public void setEsport_coach(eSport_Coach esport_coach) {
        this.esport_coach = esport_coach;
    }
    public eSport_Coach getEsport_coach() {
        return esport_coach;
    }

    public void setEsport_coach(eSport_Coach esport_coach) {
        this.esport_coach = esport_coach;
    }
    public eSport_Player getEsport_player() {
        return esport_player;
    }

    public void setEsport_player(eSport_Player esport_player) {
        this.esport_player = esport_player;
    }
    public List<eSport_Player> getEsport_players() {
        return esport_players;
    }

    public void addEsport_player(Esport_player esport_player) {
        this.esport_players.add(esport_player);
    }

}