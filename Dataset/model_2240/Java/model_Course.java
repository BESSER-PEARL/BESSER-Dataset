





import java.util.List;
import java.util.ArrayList;

public class model_Course  {

    private String fullName;
    private String name;





    private model_CourseInstance model_courseinstance;




    private model_Department model_department;


    public model_Course(
        String fullName,        String name    ) {
        this.fullName = fullName;
        this.name = name;
    }


    public String getFullname() {
        return fullName;
    }

    public void setFullname(String fullName) {
        this.fullName = fullName;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public model_CourseInstance getModel_courseinstance() {
        return model_courseinstance;
    }

    public void setModel_courseinstance(model_CourseInstance model_courseinstance) {
        this.model_courseinstance = model_courseinstance;
    }
    public model_Department getModel_department() {
        return model_department;
    }

    public void setModel_department(model_Department model_department) {
        this.model_department = model_department;
    }

}