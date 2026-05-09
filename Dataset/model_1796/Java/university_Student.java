





import java.util.List;
import java.util.ArrayList;

public class university_Student extends NamedElement {

    private float studentId;





    private university_Module university_module;




    private List<university_Module> university_modules;


    public university_Student(
        float studentId    ) {
        super(
        );
        this.studentId = studentId;
        this.university_modules = new ArrayList<>();
    }

    public university_Student(
        float studentId        ArrayList<university_Module> university_modules    ) {
        this.studentId = studentId;
        this.university_modules = university_modules;
    }

    public float getStudentid() {
        return studentId;
    }

    public void setStudentid(float studentId) {
        this.studentId = studentId;
    }

    public university_Module getUniversity_module() {
        return university_module;
    }

    public void setUniversity_module(university_Module university_module) {
        this.university_module = university_module;
    }
    public List<university_Module> getUniversity_modules() {
        return university_modules;
    }

    public void addUniversity_module(University_module university_module) {
        this.university_modules.add(university_module);
    }

}