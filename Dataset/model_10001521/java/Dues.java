





import java.util.List;
import java.util.ArrayList;

public class Dues  {

    private None student;
    private int amount;





    private Portal portal;


    public Dues(
        None student,        int amount    ) {
        this.student = student;
        this.amount = amount;
    }


    public None getStudent() {
        return student;
    }

    public void setStudent(None student) {
        this.student = student;
    }
    public int getAmount() {
        return amount;
    }

    public void setAmount(int amount) {
        this.amount = amount;
    }

    public Portal getPortal() {
        return portal;
    }

    public void setPortal(Portal portal) {
        this.portal = portal;
    }

}