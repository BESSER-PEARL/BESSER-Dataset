





import java.util.List;
import java.util.ArrayList;

public class gradingsystem_ConcreteTask extends Task {

    private int maxPoints;



    public gradingsystem_ConcreteTask(
        int maxPoints    ) {
        super(
        );
        this.maxPoints = maxPoints;
    }


    public int getMaxpoints() {
        return maxPoints;
    }

    public void setMaxpoints(int maxPoints) {
        this.maxPoints = maxPoints;
    }


}