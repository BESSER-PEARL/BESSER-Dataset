





import java.util.List;
import java.util.ArrayList;

public class dsl_AnimtationActor extends Actor {

    private String animName;
    private String cycle;
    private String speed;



    public dsl_AnimtationActor(
        String animName,        String cycle,        String speed    ) {
        super(
        );
        this.animName = animName;
        this.cycle = cycle;
        this.speed = speed;
    }


    public String getAnimname() {
        return animName;
    }

    public void setAnimname(String animName) {
        this.animName = animName;
    }
    public String getCycle() {
        return cycle;
    }

    public void setCycle(String cycle) {
        this.cycle = cycle;
    }
    public String getSpeed() {
        return speed;
    }

    public void setSpeed(String speed) {
        this.speed = speed;
    }


}