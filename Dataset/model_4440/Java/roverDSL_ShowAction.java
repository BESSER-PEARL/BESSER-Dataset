





import java.util.List;
import java.util.ArrayList;

public class roverDSL_ShowAction extends Action {

    private String string;
    private String sensor;



    public roverDSL_ShowAction(
        String string,        String sensor    ) {
        super(
        );
        this.string = string;
        this.sensor = sensor;
    }


    public String getString() {
        return string;
    }

    public void setString(String string) {
        this.string = string;
    }
    public String getSensor() {
        return sensor;
    }

    public void setSensor(String sensor) {
        this.sensor = sensor;
    }


}