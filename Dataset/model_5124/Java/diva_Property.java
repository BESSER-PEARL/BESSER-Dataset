





import java.util.List;
import java.util.ArrayList;

public class diva_Property extends NamedElement {

    private String direction;





    private diva_VariabilityModel diva_variabilitymodel;


    public diva_Property(
        String direction    ) {
        super(
        );
        this.direction = direction;
    }


    public String getDirection() {
        return direction;
    }

    public void setDirection(String direction) {
        this.direction = direction;
    }

    public diva_VariabilityModel getDiva_variabilitymodel() {
        return diva_variabilitymodel;
    }

    public void setDiva_variabilitymodel(diva_VariabilityModel diva_variabilitymodel) {
        this.diva_variabilitymodel = diva_variabilitymodel;
    }

}