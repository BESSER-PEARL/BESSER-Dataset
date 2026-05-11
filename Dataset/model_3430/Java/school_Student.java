





import java.util.List;
import java.util.ArrayList;

public class school_Student extends Person {

    private int registrationNum;



    public school_Student(
        int registrationNum    ) {
        super(
        );
        this.registrationNum = registrationNum;
    }


    public int getRegistrationnum() {
        return registrationNum;
    }

    public void setRegistrationnum(int registrationNum) {
        this.registrationNum = registrationNum;
    }


}