





import java.util.List;
import java.util.ArrayList;

public class Board  {

    private boolean battleship;
    private boolean patrolBoat;
    private boolean destroyer;
    private boolean aircraftCarrier;
    private boolean submarine;





    private List<Coordinate> coordinates;


    public Board(
        boolean battleship,        boolean patrolBoat,        boolean destroyer,        boolean aircraftCarrier,        boolean submarine    ) {
        this.battleship = battleship;
        this.patrolBoat = patrolBoat;
        this.destroyer = destroyer;
        this.aircraftCarrier = aircraftCarrier;
        this.submarine = submarine;
        this.coordinates = new ArrayList<>();
    }

    public Board(
        boolean battleship,        boolean patrolBoat,        boolean destroyer,        boolean aircraftCarrier,        boolean submarine        ArrayList<Coordinate> coordinates    ) {
        this.battleship = battleship;
        this.patrolBoat = patrolBoat;
        this.destroyer = destroyer;
        this.aircraftCarrier = aircraftCarrier;
        this.submarine = submarine;
        this.coordinates = coordinates;
    }

    public boolean getBattleship() {
        return battleship;
    }

    public void setBattleship(boolean battleship) {
        this.battleship = battleship;
    }
    public boolean getPatrolboat() {
        return patrolBoat;
    }

    public void setPatrolboat(boolean patrolBoat) {
        this.patrolBoat = patrolBoat;
    }
    public boolean getDestroyer() {
        return destroyer;
    }

    public void setDestroyer(boolean destroyer) {
        this.destroyer = destroyer;
    }
    public boolean getAircraftcarrier() {
        return aircraftCarrier;
    }

    public void setAircraftcarrier(boolean aircraftCarrier) {
        this.aircraftCarrier = aircraftCarrier;
    }
    public boolean getSubmarine() {
        return submarine;
    }

    public void setSubmarine(boolean submarine) {
        this.submarine = submarine;
    }

    public List<Coordinate> getCoordinates() {
        return coordinates;
    }

    public void addCoordinate(Coordinate coordinate) {
        this.coordinates.add(coordinate);
    }

}