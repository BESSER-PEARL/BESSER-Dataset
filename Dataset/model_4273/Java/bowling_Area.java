





import java.util.List;
import java.util.ArrayList;

public class bowling_Area  {






    private List<bowling_Area> bowling_areas;




    private List<bowling_Tournament> bowling_tournaments;


    public bowling_Area(
    ) {
        this.bowling_areas = new ArrayList<>();
        this.bowling_tournaments = new ArrayList<>();
    }

    public bowling_Area(
        ArrayList<bowling_Area> bowling_areas,        ArrayList<bowling_Tournament> bowling_tournaments    ) {
        this.bowling_areas = bowling_areas;
        this.bowling_tournaments = bowling_tournaments;
    }


    public List<bowling_Area> getBowling_areas() {
        return bowling_areas;
    }

    public void addBowling_area(Bowling_area bowling_area) {
        this.bowling_areas.add(bowling_area);
    }
    public List<bowling_Tournament> getBowling_tournaments() {
        return bowling_tournaments;
    }

    public void addBowling_tournament(Bowling_tournament bowling_tournament) {
        this.bowling_tournaments.add(bowling_tournament);
    }

}