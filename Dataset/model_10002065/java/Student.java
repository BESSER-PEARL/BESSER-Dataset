





import java.util.List;
import java.util.ArrayList;

public class Student  {

    private String SGender;
    private int SAge;





    private Admin admin;




    private Finance finance;


    public Student(
        String SGender,        int SAge    ) {
        this.SGender = SGender;
        this.SAge = SAge;
    }


    public String getSgender() {
        return SGender;
    }

    public void setSgender(String SGender) {
        this.SGender = SGender;
    }
    public int getSage() {
        return SAge;
    }

    public void setSage(int SAge) {
        this.SAge = SAge;
    }

    public Admin getAdmin() {
        return admin;
    }

    public void setAdmin(Admin admin) {
        this.admin = admin;
    }
    public Finance getFinance() {
        return finance;
    }

    public void setFinance(Finance finance) {
        this.finance = finance;
    }

}