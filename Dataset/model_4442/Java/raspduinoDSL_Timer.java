





import java.util.List;
import java.util.ArrayList;

public class raspduinoDSL_Timer  {

    private int secs;
    private int minutes;
    private String repeattype;
    private int hours;





    private raspduinoDSL_Model raspduinodsl_model;




    private raspduinoDSL_EventHandler raspduinodsl_eventhandler;


    public raspduinoDSL_Timer(
        int secs,        int minutes,        String repeattype,        int hours    ) {
        this.secs = secs;
        this.minutes = minutes;
        this.repeattype = repeattype;
        this.hours = hours;
    }


    public int getSecs() {
        return secs;
    }

    public void setSecs(int secs) {
        this.secs = secs;
    }
    public int getMinutes() {
        return minutes;
    }

    public void setMinutes(int minutes) {
        this.minutes = minutes;
    }
    public String getRepeattype() {
        return repeattype;
    }

    public void setRepeattype(String repeattype) {
        this.repeattype = repeattype;
    }
    public int getHours() {
        return hours;
    }

    public void setHours(int hours) {
        this.hours = hours;
    }

    public raspduinoDSL_Model getRaspduinodsl_model() {
        return raspduinodsl_model;
    }

    public void setRaspduinodsl_model(raspduinoDSL_Model raspduinodsl_model) {
        this.raspduinodsl_model = raspduinodsl_model;
    }
    public raspduinoDSL_EventHandler getRaspduinodsl_eventhandler() {
        return raspduinodsl_eventhandler;
    }

    public void setRaspduinodsl_eventhandler(raspduinoDSL_EventHandler raspduinodsl_eventhandler) {
        this.raspduinodsl_eventhandler = raspduinodsl_eventhandler;
    }

}