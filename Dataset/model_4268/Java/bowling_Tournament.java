





import java.util.List;
import java.util.ArrayList;

public class bowling_Tournament  {

    private String type;





    private bowling_League bowling_league;


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

    public bowling_League getBowling_league() {
        return bowling_league;
    }

    public void setBowling_league(bowling_League bowling_league) {
        this.bowling_league = bowling_league;
    }

}