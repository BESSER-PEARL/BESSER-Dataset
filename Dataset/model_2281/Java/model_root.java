





import java.util.List;
import java.util.ArrayList;

public class model_root  {






    private List<model_Course> model_courses;




    private List<model_Delivery> model_deliverys;




    private List<model_Student> model_students;


    public model_root(
    ) {
        this.model_courses = new ArrayList<>();
        this.model_deliverys = new ArrayList<>();
        this.model_students = new ArrayList<>();
    }

    public model_root(
        ArrayList<model_Course> model_courses,        ArrayList<model_Delivery> model_deliverys,        ArrayList<model_Student> model_students    ) {
        this.model_courses = model_courses;
        this.model_deliverys = model_deliverys;
        this.model_students = model_students;
    }


    public List<model_Course> getModel_courses() {
        return model_courses;
    }

    public void addModel_course(Model_course model_course) {
        this.model_courses.add(model_course);
    }
    public List<model_Delivery> getModel_deliverys() {
        return model_deliverys;
    }

    public void addModel_delivery(Model_delivery model_delivery) {
        this.model_deliverys.add(model_delivery);
    }
    public List<model_Student> getModel_students() {
        return model_students;
    }

    public void addModel_student(Model_student model_student) {
        this.model_students.add(model_student);
    }

}