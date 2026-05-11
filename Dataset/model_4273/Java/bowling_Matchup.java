





import java.util.List;
import java.util.ArrayList;

public class bowling_Matchup  {

    private String nrSpectators;





    private bowling_Tournament bowling_tournament;


    public bowling_Matchup(
        String nrSpectators    ) {
        this.nrSpectators = nrSpectators;
    }


    public String getNrspectators() {
        return nrSpectators;
    }

    public void setNrspectators(String nrSpectators) {
        this.nrSpectators = nrSpectators;
    }

    public bowling_Tournament getBowling_tournament() {
        return bowling_tournament;
    }

    public void setBowling_tournament(bowling_Tournament bowling_tournament) {
        this.bowling_tournament = bowling_tournament;
    }

}