





import java.util.List;
import java.util.ArrayList;

public class ram_StructuralView  {






    private List<ram_Type> ram_types;




    private List<ram_Association> ram_associations;




    private ram_Aspect ram_aspect;




    private List<ram_Classifier> ram_classifiers;


    public ram_StructuralView(
    ) {
        this.ram_types = new ArrayList<>();
        this.ram_associations = new ArrayList<>();
        this.ram_classifiers = new ArrayList<>();
    }

    public ram_StructuralView(
        ArrayList<ram_Type> ram_types,        ArrayList<ram_Association> ram_associations,        ArrayList<ram_Classifier> ram_classifiers    ) {
        this.ram_types = ram_types;
        this.ram_associations = ram_associations;
        this.ram_classifiers = ram_classifiers;
    }


    public List<ram_Type> getRam_types() {
        return ram_types;
    }

    public void addRam_type(Ram_type ram_type) {
        this.ram_types.add(ram_type);
    }
    public List<ram_Association> getRam_associations() {
        return ram_associations;
    }

    public void addRam_association(Ram_association ram_association) {
        this.ram_associations.add(ram_association);
    }
    public ram_Aspect getRam_aspect() {
        return ram_aspect;
    }

    public void setRam_aspect(ram_Aspect ram_aspect) {
        this.ram_aspect = ram_aspect;
    }
    public List<ram_Classifier> getRam_classifiers() {
        return ram_classifiers;
    }

    public void addRam_classifier(Ram_classifier ram_classifier) {
        this.ram_classifiers.add(ram_classifier);
    }

}