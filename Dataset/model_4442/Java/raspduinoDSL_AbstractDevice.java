





import java.util.List;
import java.util.ArrayList;

public class raspduinoDSL_AbstractDevice  {

    private String name;
    private String pin;





    private raspduinoDSL_Model raspduinodsl_model;


    public raspduinoDSL_AbstractDevice(
        String name,        String pin    ) {
        this.name = name;
        this.pin = pin;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getPin() {
        return pin;
    }

    public void setPin(String pin) {
        this.pin = pin;
    }

    public raspduinoDSL_Model getRaspduinodsl_model() {
        return raspduinodsl_model;
    }

    public void setRaspduinodsl_model(raspduinoDSL_Model raspduinodsl_model) {
        this.raspduinodsl_model = raspduinodsl_model;
    }

}