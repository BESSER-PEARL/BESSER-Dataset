





import java.util.List;
import java.util.ArrayList;

public class sec05_Patient  {

    private int urgencyIndex;





    private sec05_Person sec05_person;


    public sec05_Patient(
        int urgencyIndex    ) {
        this.urgencyIndex = urgencyIndex;
    }


    public int getUrgencyindex() {
        return urgencyIndex;
    }

    public void setUrgencyindex(int urgencyIndex) {
        this.urgencyIndex = urgencyIndex;
    }

    public sec05_Person getSec05_person() {
        return sec05_person;
    }

    public void setSec05_person(sec05_Person sec05_person) {
        this.sec05_person = sec05_person;
    }

}