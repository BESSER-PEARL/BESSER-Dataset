





import java.util.List;
import java.util.ArrayList;

public class roverml_Angle extends SingleQuantity {

    private String units;





    private roverml_Rotate roverml_rotate;


    public roverml_Angle(
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

    public roverml_Rotate getRoverml_rotate() {
        return roverml_rotate;
    }

    public void setRoverml_rotate(roverml_Rotate roverml_rotate) {
        this.roverml_rotate = roverml_rotate;
    }

}