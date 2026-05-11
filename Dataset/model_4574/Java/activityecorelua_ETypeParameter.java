





import java.util.List;
import java.util.ArrayList;

public class activityecorelua_ETypeParameter extends ENamedElement {






    private List<activityecorelua_EGenericType> activityecorelua_egenerictypes;




    private activityecorelua_EClassifier activityecorelua_eclassifier;




    private activityecorelua_EGenericType activityecorelua_egenerictype;




    private activityecorelua_EOperation activityecorelua_eoperation;


    public activityecorelua_ETypeParameter(
    ) {
        super(
        );
        this.activityecorelua_egenerictypes = new ArrayList<>();
    }

    public activityecorelua_ETypeParameter(
        ArrayList<activityecorelua_EGenericType> activityecorelua_egenerictypes    ) {
        this.activityecorelua_egenerictypes = activityecorelua_egenerictypes;
    }


    public List<activityecorelua_EGenericType> getActivityecorelua_egenerictypes() {
        return activityecorelua_egenerictypes;
    }

    public void addActivityecorelua_egenerictype(Activityecorelua_egenerictype activityecorelua_egenerictype) {
        this.activityecorelua_egenerictypes.add(activityecorelua_egenerictype);
    }
    public activityecorelua_EClassifier getActivityecorelua_eclassifier() {
        return activityecorelua_eclassifier;
    }

    public void setActivityecorelua_eclassifier(activityecorelua_EClassifier activityecorelua_eclassifier) {
        this.activityecorelua_eclassifier = activityecorelua_eclassifier;
    }
    public activityecorelua_EGenericType getActivityecorelua_egenerictype() {
        return activityecorelua_egenerictype;
    }

    public void setActivityecorelua_egenerictype(activityecorelua_EGenericType activityecorelua_egenerictype) {
        this.activityecorelua_egenerictype = activityecorelua_egenerictype;
    }
    public activityecorelua_EOperation getActivityecorelua_eoperation() {
        return activityecorelua_eoperation;
    }

    public void setActivityecorelua_eoperation(activityecorelua_EOperation activityecorelua_eoperation) {
        this.activityecorelua_eoperation = activityecorelua_eoperation;
    }

}