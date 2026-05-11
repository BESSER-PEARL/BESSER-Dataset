





import java.util.List;
import java.util.ArrayList;

public class dSL_Behavior  {

    private String name;





    private dSL_MarsRoverExpedition dsl_marsroverexpedition;


    public dSL_Behavior(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public dSL_MarsRoverExpedition getDsl_marsroverexpedition() {
        return dsl_marsroverexpedition;
    }

    public void setDsl_marsroverexpedition(dSL_MarsRoverExpedition dsl_marsroverexpedition) {
        this.dsl_marsroverexpedition = dsl_marsroverexpedition;
    }

}