





import java.util.List;
import java.util.ArrayList;

public class rosmodel_Node  {

    private String name;
    private float frequency;





    private rosmodel_Package rosmodel_package;


    public rosmodel_Node(
        String name,        float frequency    ) {
        this.name = name;
        this.frequency = frequency;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public float getFrequency() {
        return frequency;
    }

    public void setFrequency(float frequency) {
        this.frequency = frequency;
    }

    public rosmodel_Package getRosmodel_package() {
        return rosmodel_package;
    }

    public void setRosmodel_package(rosmodel_Package rosmodel_package) {
        this.rosmodel_package = rosmodel_package;
    }

}