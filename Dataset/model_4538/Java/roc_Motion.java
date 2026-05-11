





import java.util.List;
import java.util.ArrayList;

public class roc_Motion  {

    private String durationUnit;
    private String duration;





    private roc_Speed roc_speed;




    private roc_Action roc_action;




    private roc_Movement roc_movement;


    public roc_Motion(
        String durationUnit,        String duration    ) {
        this.durationUnit = durationUnit;
        this.duration = duration;
    }


    public String getDurationunit() {
        return durationUnit;
    }

    public void setDurationunit(String durationUnit) {
        this.durationUnit = durationUnit;
    }
    public String getDuration() {
        return duration;
    }

    public void setDuration(String duration) {
        this.duration = duration;
    }

    public roc_Speed getRoc_speed() {
        return roc_speed;
    }

    public void setRoc_speed(roc_Speed roc_speed) {
        this.roc_speed = roc_speed;
    }
    public roc_Action getRoc_action() {
        return roc_action;
    }

    public void setRoc_action(roc_Action roc_action) {
        this.roc_action = roc_action;
    }
    public roc_Movement getRoc_movement() {
        return roc_movement;
    }

    public void setRoc_movement(roc_Movement roc_movement) {
        this.roc_movement = roc_movement;
    }

}