





import java.util.List;
import java.util.ArrayList;

public class bowling_Tournament  {

    private String type;





    private bowling_Matchup bowling_matchup;


    public bowling_Tournament(
        String type    ) {
        this.type = type;
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

}