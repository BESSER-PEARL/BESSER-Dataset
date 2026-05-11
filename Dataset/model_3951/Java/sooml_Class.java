





import java.util.List;
import java.util.ArrayList;

public class sooml_Class extends NamedElement {






    private List<sooml_StructuralFeature> sooml_structuralfeatures;




    private sooml_Package sooml_package;


    public sooml_Class(
    ) {
        super(
        );
        this.sooml_structuralfeatures = new ArrayList<>();
    }

    public sooml_Class(
        ArrayList<sooml_StructuralFeature> sooml_structuralfeatures    ) {
        this.sooml_structuralfeatures = sooml_structuralfeatures;
    }


    public List<sooml_StructuralFeature> getSooml_structuralfeatures() {
        return sooml_structuralfeatures;
    }

    public void addSooml_structuralfeature(Sooml_structuralfeature sooml_structuralfeature) {
        this.sooml_structuralfeatures.add(sooml_structuralfeature);
    }
    public sooml_Package getSooml_package() {
        return sooml_package;
    }

    public void setSooml_package(sooml_Package sooml_package) {
        this.sooml_package = sooml_package;
    }

}