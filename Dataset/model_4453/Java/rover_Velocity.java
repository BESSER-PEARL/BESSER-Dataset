





import java.util.List;
import java.util.ArrayList;

public class rover_Velocity extends SingleQuantity {

    private String velocityUnit;





    private rover_Move rover_move;


    public rover_Velocity(
        String velocityUnit    ) {
        super(
        );
        this.velocityUnit = velocityUnit;
    }


    public String getVelocityunit() {
        return velocityUnit;
    }

    public void setVelocityunit(String velocityUnit) {
        this.velocityUnit = velocityUnit;
    }

    public rover_Move getRover_move() {
        return rover_move;
    }

    public void setRover_move(rover_Move rover_move) {
        this.rover_move = rover_move;
    }

}