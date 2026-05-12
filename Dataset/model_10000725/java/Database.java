





import java.util.List;
import java.util.ArrayList;

public class Database  {

    private String Category;
    private String Attendance;





    private Attendance attendance;


    public Database(
        String Category,        String Attendance    ) {
        this.Category = Category;
        this.Attendance = Attendance;
    }


    public String getCategory() {
        return Category;
    }

    public void setCategory(String Category) {
        this.Category = Category;
    }
    public String getAttendance() {
        return Attendance;
    }

    public void setAttendance(String Attendance) {
        this.Attendance = Attendance;
    }

    public Attendance getAttendance() {
        return attendance;
    }

    public void setAttendance(Attendance attendance) {
        this.attendance = attendance;
    }

}