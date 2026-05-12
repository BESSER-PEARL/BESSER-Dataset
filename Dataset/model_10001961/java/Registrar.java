





import java.util.List;
import java.util.ArrayList;

public class Registrar  {

    private String courseList;
    private None Status;
    private String _attr;



    public Registrar(
        String courseList,        None Status,        String _attr    ) {
        this.courseList = courseList;
        this.Status = Status;
        this._attr = _attr;
    }


    public String getCourselist() {
        return courseList;
    }

    public void setCourselist(String courseList) {
        this.courseList = courseList;
    }
    public None getStatus() {
        return Status;
    }

    public void setStatus(None Status) {
        this.Status = Status;
    }
    public String get_attr() {
        return _attr;
    }

    public void set_attr(String _attr) {
        this._attr = _attr;
    }


}