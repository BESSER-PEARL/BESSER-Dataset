





import java.util.List;
import java.util.ArrayList;

public class bowling_Alley  {

    private String name;





    private List<bowling_League> bowling_leagues;




    private List<bowling_Lane> bowling_lanes;




    private List<bowling_Tournament> bowling_tournaments;


    public bowling_Alley(
        String name    ) {
        this.name = name;
        this.bowling_leagues = new ArrayList<>();
        this.bowling_lanes = new ArrayList<>();
        this.bowling_tournaments = new ArrayList<>();
    }

    public bowling_Alley(
        String name        ArrayList<bowling_League> bowling_leagues,        ArrayList<bowling_Lane> bowling_lanes,        ArrayList<bowling_Tournament> bowling_tournaments    ) {
        this.name = name;
        this.bowling_leagues = bowling_leagues;
        this.bowling_lanes = bowling_lanes;
        this.bowling_tournaments = bowling_tournaments;
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
    public List<bowling_Lane> getBowling_lanes() {
        return bowling_lanes;
    }

    public void addBowling_lane(Bowling_lane bowling_lane) {
        this.bowling_lanes.add(bowling_lane);
    }
    public List<bowling_Tournament> getBowling_tournaments() {
        return bowling_tournaments;
    }

    public void addBowling_tournament(Bowling_tournament bowling_tournament) {
        this.bowling_tournaments.add(bowling_tournament);
    }

}