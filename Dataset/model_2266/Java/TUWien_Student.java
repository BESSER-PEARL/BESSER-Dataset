





import java.util.List;
import java.util.ArrayList;

public class TUWien_Student  {

    private String name;
    private int id;





    private TUWien_University tuwien_university;




    private TUWien_Course tuwien_course;




    private List<TUWien_Course> tuwien_courses;


    public TUWien_Student(
        String name,        int id    ) {
        this.name = name;
        this.id = id;
        this.tuwien_courses = new ArrayList<>();
    }

    public TUWien_Student(
        String name,        int id        ArrayList<TUWien_Course> tuwien_courses    ) {
        this.name = name;
        this.id = id;
        this.tuwien_courses = tuwien_courses;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public TUWien_University getTuwien_university() {
        return tuwien_university;
    }

    public void setTuwien_university(TUWien_University tuwien_university) {
        this.tuwien_university = tuwien_university;
    }
    public TUWien_Course getTuwien_course() {
        return tuwien_course;
    }

    public void setTuwien_course(TUWien_Course tuwien_course) {
        this.tuwien_course = tuwien_course;
    }
    public List<TUWien_Course> getTuwien_courses() {
        return tuwien_courses;
    }

    public void addTuwien_course(Tuwien_course tuwien_course) {
        this.tuwien_courses.add(tuwien_course);
    }

}