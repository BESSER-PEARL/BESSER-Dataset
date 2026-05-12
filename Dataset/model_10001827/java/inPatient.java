





import java.util.List;
import java.util.ArrayList;

public class inPatient  {

    private String rooomNumber;
    private String outDate;
    private String inDate;



    public inPatient(
        String rooomNumber,        String outDate,        String inDate    ) {
        this.rooomNumber = rooomNumber;
        this.outDate = outDate;
        this.inDate = inDate;
    }


    public String getRooomnumber() {
        return rooomNumber;
    }

    public void setRooomnumber(String rooomNumber) {
        this.rooomNumber = rooomNumber;
    }
    public String getOutdate() {
        return outDate;
    }

    public void setOutdate(String outDate) {
        this.outDate = outDate;
    }
    public String getIndate() {
        return inDate;
    }

    public void setIndate(String inDate) {
        this.inDate = inDate;
    }


}