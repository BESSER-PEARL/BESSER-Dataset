





import java.util.List;
import java.util.ArrayList;

public class roverml_Time extends SingleQuantity {

    private String units;





    private roverml_Wait roverml_wait;


    public roverml_Time(
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

    public roverml_Wait getRoverml_wait() {
        return roverml_wait;
    }

    public void setRoverml_wait(roverml_Wait roverml_wait) {
        this.roverml_wait = roverml_wait;
    }

}