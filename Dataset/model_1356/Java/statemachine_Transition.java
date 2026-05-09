





import java.util.List;
import java.util.ArrayList;

public class statemachine_Transition  {

    private int duration;
    private int Id;



    public statemachine_Transition(
        int duration,        int Id    ) {
        this.duration = duration;
        this.Id = Id;
    }


    public int getDuration() {
        return duration;
    }

    public void setDuration(int duration) {
        this.duration = duration;
    }
    public int getId() {
        return Id;
    }

    public void setId(int Id) {
        this.Id = Id;
    }


}