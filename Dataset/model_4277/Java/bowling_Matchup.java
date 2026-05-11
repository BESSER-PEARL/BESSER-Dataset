





import java.util.List;
import java.util.ArrayList;

public class bowling_Matchup  {

    private String name;





    private List<bowling_Game> bowling_games;




    private bowling_Tournament bowling_tournament;


    public bowling_Matchup(
        String name    ) {
        this.name = name;
        this.bowling_games = new ArrayList<>();
    }

    public bowling_Matchup(
        String name        ArrayList<bowling_Game> bowling_games    ) {
        this.name = name;
        this.bowling_games = bowling_games;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<bowling_Game> getBowling_games() {
        return bowling_games;
    }

    public void addBowling_game(Bowling_game bowling_game) {
        this.bowling_games.add(bowling_game);
    }
    public bowling_Tournament getBowling_tournament() {
        return bowling_tournament;
    }

    public void setBowling_tournament(bowling_Tournament bowling_tournament) {
        this.bowling_tournament = bowling_tournament;
    }

}