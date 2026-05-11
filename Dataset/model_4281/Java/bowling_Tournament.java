





import java.util.List;
import java.util.ArrayList;

public class bowling_Tournament  {

    private String title;
    private String type;





    private bowling_Matchup bowling_matchup;




    private List<bowling_Matchup> bowling_matchups;


    public bowling_Tournament(
        String title,        String type    ) {
        this.title = title;
        this.type = type;
        this.bowling_matchups = new ArrayList<>();
    }

    public bowling_Tournament(
        String title,        String type        ArrayList<bowling_Matchup> bowling_matchups    ) {
        this.title = title;
        this.type = type;
        this.bowling_matchups = bowling_matchups;
    }

    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public bowling_Matchup getBowling_matchup() {
        return bowling_matchup;
    }

    public void setBowling_matchup(bowling_Matchup bowling_matchup) {
        this.bowling_matchup = bowling_matchup;
    }
    public List<bowling_Matchup> getBowling_matchups() {
        return bowling_matchups;
    }

    public void addBowling_matchup(Bowling_matchup bowling_matchup) {
        this.bowling_matchups.add(bowling_matchup);
    }

}