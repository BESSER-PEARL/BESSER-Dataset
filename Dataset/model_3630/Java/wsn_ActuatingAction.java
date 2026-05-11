





import java.util.List;
import java.util.ArrayList;

public class wsn_ActuatingAction extends , Action {

    private String data;
    private String actuatorId;



    public wsn_ActuatingAction(
        String data,        String actuatorId    ) {
        super(
        );
        this.data = data;
        this.actuatorId = actuatorId;
    }


    public String getData() {
        return data;
    }

    public void setData(String data) {
        this.data = data;
    }
    public String getActuatorid() {
        return actuatorId;
    }

    public void setActuatorid(String actuatorId) {
        this.actuatorId = actuatorId;
    }


}