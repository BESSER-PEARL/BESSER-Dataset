





import java.util.List;
import java.util.ArrayList;

public class CoachBusWithEDataType_SecurityGuard extends Employee {

    private String shift;



    public CoachBusWithEDataType_SecurityGuard(
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