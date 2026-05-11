





import java.util.List;
import java.util.ArrayList;

public class raspduinoDSL_EventHandler  {

    private String name;





    private raspduinoDSL_Model raspduinodsl_model;




    private List<raspduinoDSL_ChangeActuator> raspduinodsl_changeactuators;


    public raspduinoDSL_EventHandler(
        String name    ) {
        this.name = name;
        this.raspduinodsl_changeactuators = new ArrayList<>();
    }

    public raspduinoDSL_EventHandler(
        String name        ArrayList<raspduinoDSL_ChangeActuator> raspduinodsl_changeactuators    ) {
        this.name = name;
        this.raspduinodsl_changeactuators = raspduinodsl_changeactuators;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public raspduinoDSL_Model getRaspduinodsl_model() {
        return raspduinodsl_model;
    }

    public void setRaspduinodsl_model(raspduinoDSL_Model raspduinodsl_model) {
        this.raspduinodsl_model = raspduinodsl_model;
    }
    public List<raspduinoDSL_ChangeActuator> getRaspduinodsl_changeactuators() {
        return raspduinodsl_changeactuators;
    }

    public void addRaspduinodsl_changeactuator(Raspduinodsl_changeactuator raspduinodsl_changeactuator) {
        this.raspduinodsl_changeactuators.add(raspduinodsl_changeactuator);
    }

}