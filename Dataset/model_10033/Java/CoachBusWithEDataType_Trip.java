





import java.util.List;
import java.util.ArrayList;

public class CoachBusWithEDataType_Trip  {

    private String type;





    private CoachBusWithEDataType_Coach coachbuswithedatatype_coach;


    public CoachBusWithEDataType_Trip(
        String type    ) {
        this.type = type;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public CoachBusWithEDataType_Coach getCoachbuswithedatatype_coach() {
        return coachbuswithedatatype_coach;
    }

    public void setCoachbuswithedatatype_coach(CoachBusWithEDataType_Coach coachbuswithedatatype_coach) {
        this.coachbuswithedatatype_coach = coachbuswithedatatype_coach;
    }

}