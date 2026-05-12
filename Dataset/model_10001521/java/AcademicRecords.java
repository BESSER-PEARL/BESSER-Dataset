





import java.util.List;
import java.util.ArrayList;

public class AcademicRecords  {

    private None result;
    private int dues;
    private None student;
    private None attendance;





    private Portal portal;


    public AcademicRecords(
        None result,        int dues,        None student,        None attendance    ) {
        this.result = result;
        this.dues = dues;
        this.student = student;
        this.attendance = attendance;
    }


    public None getResult() {
        return result;
    }

    public void setResult(None result) {
        this.result = result;
    }
    public int getDues() {
        return dues;
    }

    public void setDues(int dues) {
        this.dues = dues;
    }
    public None getStudent() {
        return student;
    }

    public void setStudent(None student) {
        this.student = student;
    }
    public None getAttendance() {
        return attendance;
    }

    public void setAttendance(None attendance) {
        this.attendance = attendance;
    }

    public Portal getPortal() {
        return portal;
    }

    public void setPortal(Portal portal) {
        this.portal = portal;
    }

}