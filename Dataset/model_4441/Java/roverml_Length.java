





import java.util.List;
import java.util.ArrayList;

public class roverml_Length extends SingleQuantity {

    private String units;





    private roverml_Move roverml_move;


    public roverml_Length(
        String units    ) {
        super(
        );
        this.units = units;
    }


    public String getUnits() {
        return units;
    }

    public void setUnits(String units) {
        this.units = units;
    }

    public roverml_Move getRoverml_move() {
        return roverml_move;
    }

    public void setRoverml_move(roverml_Move roverml_move) {
        this.roverml_move = roverml_move;
    }

}