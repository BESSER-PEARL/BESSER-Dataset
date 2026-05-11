





import java.util.List;
import java.util.ArrayList;

public class roverml_Angle extends SingleQuantity {

    private String angleUnit;





    private roverml_Rotate roverml_rotate;


    public roverml_Angle(
        String angleUnit    ) {
        super(
        );
        this.angleUnit = angleUnit;
    }


    public String getAngleunit() {
        return angleUnit;
    }

    public void setAngleunit(String angleUnit) {
        this.angleUnit = angleUnit;
    }

    public roverml_Rotate getRoverml_rotate() {
        return roverml_rotate;
    }

    public void setRoverml_rotate(roverml_Rotate roverml_rotate) {
        this.roverml_rotate = roverml_rotate;
    }

}