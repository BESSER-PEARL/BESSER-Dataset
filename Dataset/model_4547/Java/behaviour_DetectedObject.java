





import java.util.List;
import java.util.ArrayList;

public class behaviour_DetectedObject  {

    private boolean obstacle;





    private behaviour_AreaObject behaviour_areaobject;




    private behaviour_DynamicRobot behaviour_dynamicrobot;


    public behaviour_DetectedObject(
        boolean obstacle    ) {
        this.obstacle = obstacle;
    }


    public boolean getObstacle() {
        return obstacle;
    }

    public void setObstacle(boolean obstacle) {
        this.obstacle = obstacle;
    }

    public behaviour_AreaObject getBehaviour_areaobject() {
        return behaviour_areaobject;
    }

    public void setBehaviour_areaobject(behaviour_AreaObject behaviour_areaobject) {
        this.behaviour_areaobject = behaviour_areaobject;
    }
    public behaviour_DynamicRobot getBehaviour_dynamicrobot() {
        return behaviour_dynamicrobot;
    }

    public void setBehaviour_dynamicrobot(behaviour_DynamicRobot behaviour_dynamicrobot) {
        this.behaviour_dynamicrobot = behaviour_dynamicrobot;
    }

}