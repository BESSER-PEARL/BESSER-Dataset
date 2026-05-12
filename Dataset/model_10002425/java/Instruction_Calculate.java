





import java.util.List;
import java.util.ArrayList;

public class Instruction_Calculate  {

    private int time;





    private Operating_System operating_system;


    public Instruction_Calculate(
        int time    ) {
        this.time = time;
    }


    public int getTime() {
        return time;
    }

    public void setTime(int time) {
        this.time = time;
    }

    public Operating_System getOperating_system() {
        return operating_system;
    }

    public void setOperating_system(Operating_System operating_system) {
        this.operating_system = operating_system;
    }

}