





import java.util.List;
import java.util.ArrayList;

public class Billing_system  {

    private String course_status;
    private None course_fees;





    private List<student> students;


    public Billing_system(
        String course_status,        None course_fees    ) {
        this.course_status = course_status;
        this.course_fees = course_fees;
        this.students = new ArrayList<>();
    }

    public Billing_system(
        String course_status,        None course_fees        ArrayList<student> students    ) {
        this.course_status = course_status;
        this.course_fees = course_fees;
        this.students = students;
    }

    public String getCourse_status() {
        return course_status;
    }

    public void setCourse_status(String course_status) {
        this.course_status = course_status;
    }
    public None getCourse_fees() {
        return course_fees;
    }

    public void setCourse_fees(None course_fees) {
        this.course_fees = course_fees;
    }

    public List<student> getStudents() {
        return students;
    }

    public void addStudent(Student student) {
        this.students.add(student);
    }

}