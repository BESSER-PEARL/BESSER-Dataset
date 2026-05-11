





import java.util.List;
import java.util.ArrayList;

public class rcd_ClassModel  {

    private String name;





    private List<rcd_Classifier> rcd_classifiers;




    private List<rcd_Association> rcd_associations;


    public rcd_ClassModel(
        String name    ) {
        this.name = name;
        this.rcd_classifiers = new ArrayList<>();
        this.rcd_associations = new ArrayList<>();
    }

    public rcd_ClassModel(
        String name        ArrayList<rcd_Classifier> rcd_classifiers,        ArrayList<rcd_Association> rcd_associations    ) {
        this.name = name;
        this.rcd_classifiers = rcd_classifiers;
        this.rcd_associations = rcd_associations;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<rcd_Classifier> getRcd_classifiers() {
        return rcd_classifiers;
    }

    public void addRcd_classifier(Rcd_classifier rcd_classifier) {
        this.rcd_classifiers.add(rcd_classifier);
    }
    public List<rcd_Association> getRcd_associations() {
        return rcd_associations;
    }

    public void addRcd_association(Rcd_association rcd_association) {
        this.rcd_associations.add(rcd_association);
    }

}