





import java.util.List;
import java.util.ArrayList;

public class bowling_Referee  {

    private String dateOfBirth;





    private bowling_League bowling_league;


    public bowling_Referee(
        String dateOfBirth    ) {
        this.dateOfBirth = dateOfBirth;
    }


    public String getDateofbirth() {
        return dateOfBirth;
    }

    public void setDateofbirth(String dateOfBirth) {
        this.dateOfBirth = dateOfBirth;
    }

    public bowling_League getBowling_league() {
        return bowling_league;
    }

    public void setBowling_league(bowling_League bowling_league) {
        this.bowling_league = bowling_league;
    }

}