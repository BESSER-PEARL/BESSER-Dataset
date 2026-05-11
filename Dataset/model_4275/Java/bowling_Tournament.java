





import java.util.List;
import java.util.ArrayList;

public class bowling_Tournament  {

    private String type;
    private String title;





    private bowling_League bowling_league;




    private List<bowling_Matchup> bowling_matchups;


    public bowling_Tournament(
        String type,        String title    ) {
        this.type = type;
        this.title = title;
        this.bowling_matchups = new ArrayList<>();
    }

    public bowling_Tournament(
        String type,        String title        ArrayList<bowling_Matchup> bowling_matchups    ) {
        this.type = type;
        this.title = title;
        this.bowling_matchups = bowling_matchups;
    }

    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }

    public bowling_League getBowling_league() {
        return bowling_league;
    }

    public void setBowling_league(bowling_League bowling_league) {
        this.bowling_league = bowling_league;
    }
    public List<bowling_Matchup> getBowling_matchups() {
        return bowling_matchups;
    }

    public void addBowling_matchup(Bowling_matchup bowling_matchup) {
        this.bowling_matchups.add(bowling_matchup);
    }

}