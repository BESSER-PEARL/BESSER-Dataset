





import java.util.List;
import java.util.ArrayList;

public class raspduinoDSL_SensorListener  {

    private String type;
    private int h;
    private int l;





    private raspduinoDSL_Model raspduinodsl_model;




    private raspduinoDSL_Sensor raspduinodsl_sensor;




    private raspduinoDSL_EventHandler raspduinodsl_eventhandler;


    public raspduinoDSL_SensorListener(
        String type,        int h,        int l    ) {
        this.type = type;
        this.h = h;
        this.l = l;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public int getH() {
        return h;
    }

    public void setH(int h) {
        this.h = h;
    }
    public int getL() {
        return l;
    }

    public void setL(int l) {
        this.l = l;
    }

    public raspduinoDSL_Model getRaspduinodsl_model() {
        return raspduinodsl_model;
    }

    public void setRaspduinodsl_model(raspduinoDSL_Model raspduinodsl_model) {
        this.raspduinodsl_model = raspduinodsl_model;
    }
    public raspduinoDSL_Sensor getRaspduinodsl_sensor() {
        return raspduinodsl_sensor;
    }

    public void setRaspduinodsl_sensor(raspduinoDSL_Sensor raspduinodsl_sensor) {
        this.raspduinodsl_sensor = raspduinodsl_sensor;
    }
    public raspduinoDSL_EventHandler getRaspduinodsl_eventhandler() {
        return raspduinodsl_eventhandler;
    }

    public void setRaspduinodsl_eventhandler(raspduinoDSL_EventHandler raspduinodsl_eventhandler) {
        this.raspduinodsl_eventhandler = raspduinodsl_eventhandler;
    }

}