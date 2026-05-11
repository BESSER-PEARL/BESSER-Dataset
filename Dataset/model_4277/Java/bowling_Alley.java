





import java.util.List;
import java.util.ArrayList;

public class bowling_Alley  {

    private String name;





    private List<bowling_League> bowling_leagues;


    public bowling_Alley(
        String name    ) {
        this.name = name;
        this.bowling_leagues = new ArrayList<>();
    }

    public bowling_Alley(
        String name        ArrayList<bowling_League> bowling_leagues    ) {
        this.name = name;
        this.bowling_leagues = bowling_leagues;
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

}