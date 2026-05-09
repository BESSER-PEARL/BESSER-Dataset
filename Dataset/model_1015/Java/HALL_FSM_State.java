





import java.util.List;
import java.util.ArrayList;

public class HALL_FSM_State  {

    private boolean isActive;



    public HALL_FSM_State(
        boolean isActive    ) {
        this.isActive = isActive;
    }


    public boolean getIsactive() {
        return isActive;
    }

    public void setIsactive(boolean isActive) {
        this.isActive = isActive;
    }


}