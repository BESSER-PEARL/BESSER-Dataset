





import java.util.List;
import java.util.ArrayList;

public class elevatortest_Patient  {

    private int urgencyIndex;





    private elevatortest_Person elevatortest_person;


    public elevatortest_Patient(
        int urgencyIndex    ) {
        this.urgencyIndex = urgencyIndex;
    }


    public int getUrgencyindex() {
        return urgencyIndex;
    }

    public void setUrgencyindex(int urgencyIndex) {
        this.urgencyIndex = urgencyIndex;
    }

    public elevatortest_Person getElevatortest_person() {
        return elevatortest_person;
    }

    public void setElevatortest_person(elevatortest_Person elevatortest_person) {
        this.elevatortest_person = elevatortest_person;
    }

}