





import java.util.List;
import java.util.ArrayList;

public class activityecorelua_EModelElement  {






    private activityecorelua_EAnnotation activityecorelua_eannotation;




    private List<activityecorelua_EAnnotation> activityecorelua_eannotations;


    public activityecorelua_EModelElement(
    ) {
        this.activityecorelua_eannotations = new ArrayList<>();
    }

    public activityecorelua_EModelElement(
        ArrayList<activityecorelua_EAnnotation> activityecorelua_eannotations    ) {
        this.activityecorelua_eannotations = activityecorelua_eannotations;
    }


    public activityecorelua_EAnnotation getActivityecorelua_eannotation() {
        return activityecorelua_eannotation;
    }

    public void setActivityecorelua_eannotation(activityecorelua_EAnnotation activityecorelua_eannotation) {
        this.activityecorelua_eannotation = activityecorelua_eannotation;
    }
    public List<activityecorelua_EAnnotation> getActivityecorelua_eannotations() {
        return activityecorelua_eannotations;
    }

    public void addActivityecorelua_eannotation(Activityecorelua_eannotation activityecorelua_eannotation) {
        this.activityecorelua_eannotations.add(activityecorelua_eannotation);
    }

}