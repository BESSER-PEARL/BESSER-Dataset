





import java.util.List;
import java.util.ArrayList;

public class drones_MovableObject extends FieldObject {

    private float weight;



    public drones_MovableObject(
        float weight    ) {
        super(
        );
        this.weight = weight;
    }


    public float getWeight() {
        return weight;
    }

    public void setWeight(float weight) {
        this.weight = weight;
    }


}