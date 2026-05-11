





import java.util.List;
import java.util.ArrayList;

public class dsl_Turrent  {

    private String boneName;
    private String name;
    private int idleSpeed;
    private int speed;
    private String onIdle;





    private dsl_Model dsl_model;


    public dsl_Turrent(
        String boneName,        String name,        int idleSpeed,        int speed,        String onIdle    ) {
        this.boneName = boneName;
        this.name = name;
        this.idleSpeed = idleSpeed;
        this.speed = speed;
        this.onIdle = onIdle;
    }


    public String getBonename() {
        return boneName;
    }

    public void setBonename(String boneName) {
        this.boneName = boneName;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public int getIdlespeed() {
        return idleSpeed;
    }

    public void setIdlespeed(int idleSpeed) {
        this.idleSpeed = idleSpeed;
    }
    public int getSpeed() {
        return speed;
    }

    public void setSpeed(int speed) {
        this.speed = speed;
    }
    public String getOnidle() {
        return onIdle;
    }

    public void setOnidle(String onIdle) {
        this.onIdle = onIdle;
    }

    public dsl_Model getDsl_model() {
        return dsl_model;
    }

    public void setDsl_model(dsl_Model dsl_model) {
        this.dsl_model = dsl_model;
    }

}