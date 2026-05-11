





import java.util.List;
import java.util.ArrayList;

public class uml_UML_Classifier extends UML_Namespace, UML_Type {






    private List<uml_UML_Feature> uml_uml_features;




    private uml_UML_Class uml_uml_class;


    public uml_UML_Classifier(
    ) {
        super(
        );
        this.uml_uml_features = new ArrayList<>();
    }

    public uml_UML_Classifier(
        ArrayList<uml_UML_Feature> uml_uml_features    ) {
        this.uml_uml_features = uml_uml_features;
    }


    public List<uml_UML_Feature> getUml_uml_features() {
        return uml_uml_features;
    }

    public void addUml_uml_feature(Uml_uml_feature uml_uml_feature) {
        this.uml_uml_features.add(uml_uml_feature);
    }
    public uml_UML_Class getUml_uml_class() {
        return uml_uml_class;
    }

    public void setUml_uml_class(uml_UML_Class uml_uml_class) {
        this.uml_uml_class = uml_uml_class;
    }

}