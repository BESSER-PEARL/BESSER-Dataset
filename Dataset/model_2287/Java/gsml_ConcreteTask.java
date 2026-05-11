





import java.util.List;
import java.util.ArrayList;

public class gsml_ConcreteTask extends Task {

    private float MaxPoints;



    public gsml_ConcreteTask(
        float MaxPoints    ) {
        super(
        );
        this.MaxPoints = MaxPoints;
    }


    public float getMaxpoints() {
        return MaxPoints;
    }

    public void setMaxpoints(float MaxPoints) {
        this.MaxPoints = MaxPoints;
    }


}