





import java.util.List;
import java.util.ArrayList;

public class robot_robot_Bip extends Command {

    private String repet;
    private String duration;
    private String power;



    public robot_robot_Bip(
        String repet,        String duration,        String power    ) {
        super(
        );
        this.repet = repet;
        this.duration = duration;
        this.power = power;
    }


    public String getRepet() {
        return repet;
    }

    public void setRepet(String repet) {
        this.repet = repet;
    }
    public String getDuration() {
        return duration;
    }

    public void setDuration(String duration) {
        this.duration = duration;
    }
    public String getPower() {
        return power;
    }

    public void setPower(String power) {
        this.power = power;
    }


}