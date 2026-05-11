





import java.util.List;
import java.util.ArrayList;

public class dronesStructure_Dimension  {

    private float depth;
    private float height;
    private float width;





    private dronesStructure_DroneType dronesstructure_dronetype;


    public dronesStructure_Dimension(
        float depth,        float height,        float width    ) {
        this.depth = depth;
        this.height = height;
        this.width = width;
    }


    public float getDepth() {
        return depth;
    }

    public void setDepth(float depth) {
        this.depth = depth;
    }
    public float getHeight() {
        return height;
    }

    public void setHeight(float height) {
        this.height = height;
    }
    public float getWidth() {
        return width;
    }

    public void setWidth(float width) {
        this.width = width;
    }

    public dronesStructure_DroneType getDronesstructure_dronetype() {
        return dronesstructure_dronetype;
    }

    public void setDronesstructure_dronetype(dronesStructure_DroneType dronesstructure_dronetype) {
        this.dronesstructure_dronetype = dronesstructure_dronetype;
    }

}