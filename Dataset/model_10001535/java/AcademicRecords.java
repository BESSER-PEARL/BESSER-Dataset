





import java.util.List;
import java.util.ArrayList;

public class AcademicRecords  {

    private int dues;
    private String attendance;
    private None result;
    private None student;





    private Portal portal;


    public AcademicRecords(
        int dues,        String attendance,        None result,        None student    ) {
        this.dues = dues;
        this.attendance = attendance;
        this.result = result;
        this.student = student;
    }


    public int getDues() {
        return dues;
    }

    public void setDues(int dues) {
        this.dues = dues;
    }
    public String getAttendance() {
        return attendance;
    }

    public void setAttendance(String attendance) {
        this.attendance = attendance;
    }
    public None getResult() {
        return result;
    }

    public void setResult(None result) {
        this.result = result;
    }
    public None getStudent() {
        return student;
    }

    public void setStudent(None student) {
        this.student = student;
    }

    public Portal getPortal() {
        return portal;
    }

    public void setPortal(Portal portal) {
        this.portal = portal;
    }

}