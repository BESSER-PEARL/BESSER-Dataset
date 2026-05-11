





import java.util.List;
import java.util.ArrayList;

public class roverml_Velocity extends SingleQuantity {

    private String velocityUnit;





    private roverml_Move roverml_move;


    public roverml_Velocity(
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

    public roverml_Move getRoverml_move() {
        return roverml_move;
    }

    public void setRoverml_move(roverml_Move roverml_move) {
        this.roverml_move = roverml_move;
    }

}