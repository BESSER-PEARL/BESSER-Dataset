





import java.util.List;
import java.util.ArrayList;

public class bowling_Playerlist  {

    private String name;





    private bowling_Tournament bowling_tournament;




    private bowling_Tournament bowling_tournament;




    private bowling_Player bowling_player;




    private List<bowling_Player> bowling_players;


    public bowling_Playerlist(
        String name    ) {
        this.name = name;
        this.bowling_players = new ArrayList<>();
    }

    public bowling_Playerlist(
        String name        ArrayList<bowling_Player> bowling_players    ) {
        this.name = name;
        this.bowling_players = bowling_players;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public bowling_Tournament getBowling_tournament() {
        return bowling_tournament;
    }

    public void setBowling_tournament(bowling_Tournament bowling_tournament) {
        this.bowling_tournament = bowling_tournament;
    }
    public bowling_Tournament getBowling_tournament() {
        return bowling_tournament;
    }

    public void setBowling_tournament(bowling_Tournament bowling_tournament) {
        this.bowling_tournament = bowling_tournament;
    }
    public bowling_Player getBowling_player() {
        return bowling_player;
    }

    public void setBowling_player(bowling_Player bowling_player) {
        this.bowling_player = bowling_player;
    }
    public List<bowling_Player> getBowling_players() {
        return bowling_players;
    }

    public void addBowling_player(Bowling_player bowling_player) {
        this.bowling_players.add(bowling_player);
    }

}