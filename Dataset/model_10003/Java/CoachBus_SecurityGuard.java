





import java.util.List;
import java.util.ArrayList;

public class CoachBus_SecurityGuard extends Employee {

    private String shift;



    public CoachBus_SecurityGuard(
        String shift    ) {
        super(
        );
        this.shift = shift;
    }


    public String getShift() {
        return shift;
    }

    public void setShift(String shift) {
        this.shift = shift;
    }


}