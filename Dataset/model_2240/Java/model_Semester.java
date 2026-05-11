





import java.util.List;
import java.util.ArrayList;

public class model_Semester  {

    private String kind;
    private String year;





    private List<model_CourseInstance> model_courseinstances;




    private model_Department model_department;




    private model_CourseInstance model_courseinstance;


    public model_Semester(
        String kind,        String year    ) {
        this.kind = kind;
        this.year = year;
        this.model_courseinstances = new ArrayList<>();
    }

    public model_Semester(
        String kind,        String year        ArrayList<model_CourseInstance> model_courseinstances    ) {
        this.kind = kind;
        this.year = year;
        this.model_courseinstances = model_courseinstances;
    }

    public String getKind() {
        return kind;
    }

    public void setKind(String kind) {
        this.kind = kind;
    }
    public String getYear() {
        return year;
    }

    public void setYear(String year) {
        this.year = year;
    }

    public List<model_CourseInstance> getModel_courseinstances() {
        return model_courseinstances;
    }

    public void addModel_courseinstance(Model_courseinstance model_courseinstance) {
        this.model_courseinstances.add(model_courseinstance);
    }
    public model_Department getModel_department() {
        return model_department;
    }

    public void setModel_department(model_Department model_department) {
        this.model_department = model_department;
    }
    public model_CourseInstance getModel_courseinstance() {
        return model_courseinstance;
    }

    public void setModel_courseinstance(model_CourseInstance model_courseinstance) {
        this.model_courseinstance = model_courseinstance;
    }

}