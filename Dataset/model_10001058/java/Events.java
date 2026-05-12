





import java.util.List;
import java.util.ArrayList;

public class Events  {

    private String _attr;
    private int eventdescription;
    private String Evantname;
    private int eventId;
    private int eventtitle;





    private List<student> students;


    public Events(
        String _attr,        int eventdescription,        String Evantname,        int eventId,        int eventtitle    ) {
        this._attr = _attr;
        this.eventdescription = eventdescription;
        this.Evantname = Evantname;
        this.eventId = eventId;
        this.eventtitle = eventtitle;
        this.students = new ArrayList<>();
    }

    public Events(
        String _attr,        int eventdescription,        String Evantname,        int eventId,        int eventtitle        ArrayList<student> students    ) {
        this._attr = _attr;
        this.eventdescription = eventdescription;
        this.Evantname = Evantname;
        this.eventId = eventId;
        this.eventtitle = eventtitle;
        this.students = students;
    }

    public String get_attr() {
        return _attr;
    }

    public void set_attr(String _attr) {
        this._attr = _attr;
    }
    public int getEventdescription() {
        return eventdescription;
    }

    public void setEventdescription(int eventdescription) {
        this.eventdescription = eventdescription;
    }
    public String getEvantname() {
        return Evantname;
    }

    public void setEvantname(String Evantname) {
        this.Evantname = Evantname;
    }
    public int getEventid() {
        return eventId;
    }

    public void setEventid(int eventId) {
        this.eventId = eventId;
    }
    public int getEventtitle() {
        return eventtitle;
    }

    public void setEventtitle(int eventtitle) {
        this.eventtitle = eventtitle;
    }

    public List<student> getStudents() {
        return students;
    }

    public void addStudent(Student student) {
        this.students.add(student);
    }

}