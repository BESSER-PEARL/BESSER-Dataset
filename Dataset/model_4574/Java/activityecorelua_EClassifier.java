





import java.util.List;
import java.util.ArrayList;

public class activityecorelua_EClassifier extends ENamedElement {

    private String instanceClassName;
    private String instanceTypeName;
    private String instanceClass;
    private String defaultValue;





    private activityecorelua_EOperation activityecorelua_eoperation;




    private activityecorelua_EGenericType activityecorelua_egenerictype;




    private activityecorelua_EGenericType activityecorelua_egenerictype;


    public activityecorelua_EClassifier(
        String instanceClassName,        String instanceTypeName,        String instanceClass,        String defaultValue    ) {
        super(
        );
        this.instanceClassName = instanceClassName;
        this.instanceTypeName = instanceTypeName;
        this.instanceClass = instanceClass;
        this.defaultValue = defaultValue;
    }


    public String getInstanceclassname() {
        return instanceClassName;
    }

    public void setInstanceclassname(String instanceClassName) {
        this.instanceClassName = instanceClassName;
    }
    public String getInstancetypename() {
        return instanceTypeName;
    }

    public void setInstancetypename(String instanceTypeName) {
        this.instanceTypeName = instanceTypeName;
    }
    public String getInstanceclass() {
        return instanceClass;
    }

    public void setInstanceclass(String instanceClass) {
        this.instanceClass = instanceClass;
    }
    public String getDefaultvalue() {
        return defaultValue;
    }

    public void setDefaultvalue(String defaultValue) {
        this.defaultValue = defaultValue;
    }

    public activityecorelua_EOperation getActivityecorelua_eoperation() {
        return activityecorelua_eoperation;
    }

    public void setActivityecorelua_eoperation(activityecorelua_EOperation activityecorelua_eoperation) {
        this.activityecorelua_eoperation = activityecorelua_eoperation;
    }
    public activityecorelua_EGenericType getActivityecorelua_egenerictype() {
        return activityecorelua_egenerictype;
    }

    public void setActivityecorelua_egenerictype(activityecorelua_EGenericType activityecorelua_egenerictype) {
        this.activityecorelua_egenerictype = activityecorelua_egenerictype;
    }
    public activityecorelua_EGenericType getActivityecorelua_egenerictype() {
        return activityecorelua_egenerictype;
    }

    public void setActivityecorelua_egenerictype(activityecorelua_EGenericType activityecorelua_egenerictype) {
        this.activityecorelua_egenerictype = activityecorelua_egenerictype;
    }

}