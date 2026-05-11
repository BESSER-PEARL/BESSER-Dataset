




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class model_Exercise  {

    private LocalDate deadline_date;
    private int ID;





    private List<model_Delivery> model_deliverys;




    private model_Course model_course;




    private List<model_Student> model_students;


    public model_Exercise(
        LocalDate deadline_date,        int ID    ) {
        this.deadline_date = deadline_date;
        this.ID = ID;
        this.model_deliverys = new ArrayList<>();
        this.model_students = new ArrayList<>();
    }

    public model_Exercise(
        LocalDate deadline_date,        int ID        ArrayList<model_Delivery> model_deliverys,        ArrayList<model_Student> model_students    ) {
        this.deadline_date = deadline_date;
        this.ID = ID;
        this.model_deliverys = model_deliverys;
        this.model_students = model_students;
    }

    public LocalDate getDeadline_date() {
        return deadline_date;
    }

    public void setDeadline_date(LocalDate deadline_date) {
        this.deadline_date = deadline_date;
    }
    public int getId() {
        return ID;
    }

    public void setId(int ID) {
        this.ID = ID;
    }

    public List<model_Delivery> getModel_deliverys() {
        return model_deliverys;
    }

    public void addModel_delivery(Model_delivery model_delivery) {
        this.model_deliverys.add(model_delivery);
    }
    public model_Course getModel_course() {
        return model_course;
    }

    public void setModel_course(model_Course model_course) {
        this.model_course = model_course;
    }
    public List<model_Student> getModel_students() {
        return model_students;
    }

    public void addModel_student(Model_student model_student) {
        this.model_students.add(model_student);
    }

}