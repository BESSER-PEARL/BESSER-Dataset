





import java.util.List;
import java.util.ArrayList;

public class mission_LineTask extends Task {






    private List<mission_Coordinate> mission_coordinates;




    private mission_Coordinate mission_coordinate;


    public mission_LineTask(
    ) {
        super(
        );
        this.mission_coordinates = new ArrayList<>();
    }

    public mission_LineTask(
        ArrayList<mission_Coordinate> mission_coordinates    ) {
        this.mission_coordinates = mission_coordinates;
    }


    public List<mission_Coordinate> getMission_coordinates() {
        return mission_coordinates;
    }

    public void addMission_coordinate(Mission_coordinate mission_coordinate) {
        this.mission_coordinates.add(mission_coordinate);
    }
    public mission_Coordinate getMission_coordinate() {
        return mission_coordinate;
    }

    public void setMission_coordinate(mission_Coordinate mission_coordinate) {
        this.mission_coordinate = mission_coordinate;
    }

}