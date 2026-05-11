





import java.util.List;
import java.util.ArrayList;

public class model_CourseAllocation  {

    private String factor;
    private String explicitFactor;





    private model_CourseInstance model_courseinstance;




    private model_CourseInstance model_courseinstance;




    private model_Person model_person;




    private model_Role model_role;




    private model_Person model_person;


    public model_CourseAllocation(
        String factor,        String explicitFactor    ) {
        this.factor = factor;
        this.explicitFactor = explicitFactor;
    }


    public String getFactor() {
        return factor;
    }

    public void setFactor(String factor) {
        this.factor = factor;
    }
    public String getExplicitfactor() {
        return explicitFactor;
    }

    public void setExplicitfactor(String explicitFactor) {
        this.explicitFactor = explicitFactor;
    }

    public model_CourseInstance getModel_courseinstance() {
        return model_courseinstance;
    }

    public void setModel_courseinstance(model_CourseInstance model_courseinstance) {
        this.model_courseinstance = model_courseinstance;
    }
    public model_CourseInstance getModel_courseinstance() {
        return model_courseinstance;
    }

    public void setModel_courseinstance(model_CourseInstance model_courseinstance) {
        this.model_courseinstance = model_courseinstance;
    }
    public model_Person getModel_person() {
        return model_person;
    }

    public void setModel_person(model_Person model_person) {
        this.model_person = model_person;
    }
    public model_Role getModel_role() {
        return model_role;
    }

    public void setModel_role(model_Role model_role) {
        this.model_role = model_role;
    }
    public model_Person getModel_person() {
        return model_person;
    }

    public void setModel_person(model_Person model_person) {
        this.model_person = model_person;
    }

}