





import java.util.List;
import java.util.ArrayList;

public class diva_Property extends NamedElement {

    private String direction;





    private diva_Dimension diva_dimension;


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

    public diva_Dimension getDiva_dimension() {
        return diva_dimension;
    }

    public void setDiva_dimension(diva_Dimension diva_dimension) {
        this.diva_dimension = diva_dimension;
    }

}