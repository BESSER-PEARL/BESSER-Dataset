





import java.util.List;
import java.util.ArrayList;

public class bowling_league  {

    private String name;





    private List<bowling_Player> bowling_players;


    public bowling_league(
        String name    ) {
        this.name = name;
        this.bowling_players = new ArrayList<>();
    }

    public bowling_league(
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

    public List<bowling_Player> getBowling_players() {
        return bowling_players;
    }

    public void addBowling_player(Bowling_player bowling_player) {
        this.bowling_players.add(bowling_player);
    }

}