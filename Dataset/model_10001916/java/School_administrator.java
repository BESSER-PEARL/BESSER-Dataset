





import java.util.List;
import java.util.ArrayList;

public class School_administrator  {






    private List<Parents> parentss;




    private students students;




    private attendance_manager attendance_manager;


    public School_administrator(
    ) {
        this.parentss = new ArrayList<>();
    }

    public School_administrator(
        ArrayList<Parents> parentss    ) {
        this.parentss = parentss;
    }


    public List<Parents> getParentss() {
        return parentss;
    }

    public void addParents(Parents parents) {
        this.parentss.add(parents);
    }
    public students getStudents() {
        return students;
    }

    public void setStudents(students students) {
        this.students = students;
    }
    public attendance_manager getAttendance_manager() {
        return attendance_manager;
    }

    public void setAttendance_manager(attendance_manager attendance_manager) {
        this.attendance_manager = attendance_manager;
    }

}