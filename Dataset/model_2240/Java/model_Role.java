





import java.util.List;
import java.util.ArrayList;

public class model_Role  {

    private String name;
    private String factor;





    private model_Course model_course;




    private model_Department model_department;


    public model_Role(
        String name,        String factor    ) {
        this.name = name;
        this.factor = factor;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getFactor() {
        return factor;
    }

    public void setFactor(String factor) {
        this.factor = factor;
    }

    public model_Course getModel_course() {
        return model_course;
    }

    public void setModel_course(model_Course model_course) {
        this.model_course = model_course;
    }
    public model_Department getModel_department() {
        return model_department;
    }

    public void setModel_department(model_Department model_department) {
        this.model_department = model_department;
    }

}