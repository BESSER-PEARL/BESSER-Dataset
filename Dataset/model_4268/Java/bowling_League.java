





import java.util.List;
import java.util.ArrayList;

public class bowling_League  {

    private String name;





    private List<bowling_League> bowling_leagues;




    private List<bowling_Player> bowling_players;


    public bowling_League(
        String name    ) {
        this.name = name;
        this.bowling_leagues = new ArrayList<>();
        this.bowling_players = new ArrayList<>();
    }

    public bowling_League(
        String name        ArrayList<bowling_League> bowling_leagues,        ArrayList<bowling_Player> bowling_players    ) {
        this.name = name;
        this.bowling_leagues = bowling_leagues;
        this.bowling_players = bowling_players;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<bowling_League> getBowling_leagues() {
        return bowling_leagues;
    }

    public void addBowling_league(Bowling_league bowling_league) {
        this.bowling_leagues.add(bowling_league);
    }
    public List<bowling_Player> getBowling_players() {
        return bowling_players;
    }

    public void addBowling_player(Bowling_player bowling_player) {
        this.bowling_players.add(bowling_player);
    }

}