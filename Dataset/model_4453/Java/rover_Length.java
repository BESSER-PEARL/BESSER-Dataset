





import java.util.List;
import java.util.ArrayList;

public class rover_Length extends SingleQuantity {

    private String lengthUnit;





    private rover_Position rover_position;




    private rover_Distance rover_distance;




    private rover_Position rover_position;




    private rover_Move rover_move;


    public rover_Length(
        String lengthUnit    ) {
        super(
        );
        this.lengthUnit = lengthUnit;
    }


    public String getLengthunit() {
        return lengthUnit;
    }

    public void setLengthunit(String lengthUnit) {
        this.lengthUnit = lengthUnit;
    }

    public rover_Position getRover_position() {
        return rover_position;
    }

    public void setRover_position(rover_Position rover_position) {
        this.rover_position = rover_position;
    }
    public rover_Distance getRover_distance() {
        return rover_distance;
    }

    public void setRover_distance(rover_Distance rover_distance) {
        this.rover_distance = rover_distance;
    }
    public rover_Position getRover_position() {
        return rover_position;
    }

    public void setRover_position(rover_Position rover_position) {
        this.rover_position = rover_position;
    }
    public rover_Move getRover_move() {
        return rover_move;
    }

    public void setRover_move(rover_Move rover_move) {
        this.rover_move = rover_move;
    }

}