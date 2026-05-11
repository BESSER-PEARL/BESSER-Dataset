





import java.util.List;
import java.util.ArrayList;

public class gyro_Child  {






    private List<gyro_Behavior> gyro_behaviors;


    public gyro_Child(
    ) {
        this.gyro_behaviors = new ArrayList<>();
    }

    public gyro_Child(
        ArrayList<gyro_Behavior> gyro_behaviors    ) {
        this.gyro_behaviors = gyro_behaviors;
    }


    public List<gyro_Behavior> getGyro_behaviors() {
        return gyro_behaviors;
    }

    public void addGyro_behavior(Gyro_behavior gyro_behavior) {
        this.gyro_behaviors.add(gyro_behavior);
    }

}