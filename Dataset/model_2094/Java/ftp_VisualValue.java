





import java.util.List;
import java.util.ArrayList;

public class ftp_VisualValue extends TypedPortValue {

    private String bulb;



    public ftp_VisualValue(
        String bulb    ) {
        super(
        );
        this.bulb = bulb;
    }


    public String getBulb() {
        return bulb;
    }

    public void setBulb(String bulb) {
        this.bulb = bulb;
    }


}