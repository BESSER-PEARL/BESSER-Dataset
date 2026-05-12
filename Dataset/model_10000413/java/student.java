





import java.util.List;
import java.util.ArrayList;

public class student  {

    private String s_name;
    private int s_id;





    private Tescher tescher;




    private List<courses> coursess;


    public student(
        String s_name,        int s_id    ) {
        this.s_name = s_name;
        this.s_id = s_id;
        this.coursess = new ArrayList<>();
    }

    public student(
        String s_name,        int s_id        ArrayList<courses> coursess    ) {
        this.s_name = s_name;
        this.s_id = s_id;
        this.coursess = coursess;
    }

    public String getS_name() {
        return s_name;
    }

    public void setS_name(String s_name) {
        this.s_name = s_name;
    }
    public int getS_id() {
        return s_id;
    }

    public void setS_id(int s_id) {
        this.s_id = s_id;
    }

    public Tescher getTescher() {
        return tescher;
    }

    public void setTescher(Tescher tescher) {
        this.tescher = tescher;
    }
    public List<courses> getCoursess() {
        return coursess;
    }

    public void addCourses(Courses courses) {
        this.coursess.add(courses);
    }

}