





import java.util.List;
import java.util.ArrayList;

public class ardurobotml_FSMClock extends NamedElement {

    private int value;





    private ardurobotml_TimedSystem ardurobotml_timedsystem;


    public ardurobotml_FSMClock(
        int value    ) {
        super(
        );
        this.value = value;
    }


    public int getValue() {
        return value;
    }

    public void setValue(int value) {
        this.value = value;
    }

    public ardurobotml_TimedSystem getArdurobotml_timedsystem() {
        return ardurobotml_timedsystem;
    }

    public void setArdurobotml_timedsystem(ardurobotml_TimedSystem ardurobotml_timedsystem) {
        this.ardurobotml_timedsystem = ardurobotml_timedsystem;
    }

}