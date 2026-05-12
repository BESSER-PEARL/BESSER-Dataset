





import java.util.List;
import java.util.ArrayList;

public class Bill  {

    private int no;
    private int patientno;
    private String amount;



    public Bill(
        int no,        int patientno,        String amount    ) {
        this.no = no;
        this.patientno = patientno;
        this.amount = amount;
    }


    public int getNo() {
        return no;
    }

    public void setNo(int no) {
        this.no = no;
    }
    public int getPatientno() {
        return patientno;
    }

    public void setPatientno(int patientno) {
        this.patientno = patientno;
    }
    public String getAmount() {
        return amount;
    }

    public void setAmount(String amount) {
        this.amount = amount;
    }


}