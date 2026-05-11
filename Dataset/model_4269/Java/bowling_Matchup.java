





import java.util.List;
import java.util.ArrayList;

public class bowling_Matchup  {

    private String name;





    private bowling_Tournament bowling_tournament;


    public bowling_Matchup(
        String name    ) {
        this.name = name;
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

}