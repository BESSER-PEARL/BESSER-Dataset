





import java.util.List;
import java.util.ArrayList;

public class robotDSL_Sensor  {

    private String sensorType;





    private robotDSL_Trigger robotdsl_trigger;


    public robotDSL_Sensor(
        String sensorType    ) {
        this.sensorType = sensorType;
    }


    public String getSensortype() {
        return sensorType;
    }

    public void setSensortype(String sensorType) {
        this.sensorType = sensorType;
    }

    public robotDSL_Trigger getRobotdsl_trigger() {
        return robotdsl_trigger;
    }

    public void setRobotdsl_trigger(robotDSL_Trigger robotdsl_trigger) {
        this.robotdsl_trigger = robotdsl_trigger;
    }

}