





import java.util.List;
import java.util.ArrayList;

public class roverml_Length extends SingleQuantity {

    private String lengthUnit;





    private roverml_Move roverml_move;


    public roverml_Length(
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

    public roverml_Move getRoverml_move() {
        return roverml_move;
    }

    public void setRoverml_move(roverml_Move roverml_move) {
        this.roverml_move = roverml_move;
    }

}