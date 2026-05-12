





import java.util.List;
import java.util.ArrayList;

public class CoachBusWithEDataType_Passenger  {

    private int age;
    private String sex;





    private CoachBusWithEDataType_Trip coachbuswithedatatype_trip;


    public CoachBusWithEDataType_Passenger(
        int age,        String sex    ) {
        this.age = age;
        this.sex = sex;
    }


    public int getAge() {
        return age;
    }

    public void setAge(int age) {
        this.age = age;
    }
    public String getSex() {
        return sex;
    }

    public void setSex(String sex) {
        this.sex = sex;
    }

    public CoachBusWithEDataType_Trip getCoachbuswithedatatype_trip() {
        return coachbuswithedatatype_trip;
    }

    public void setCoachbuswithedatatype_trip(CoachBusWithEDataType_Trip coachbuswithedatatype_trip) {
        this.coachbuswithedatatype_trip = coachbuswithedatatype_trip;
    }

}