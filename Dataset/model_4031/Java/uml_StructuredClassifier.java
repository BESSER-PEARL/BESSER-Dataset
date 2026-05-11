





import java.util.List;
import java.util.ArrayList;

public class uml_StructuredClassifier extends Classifier {






    private List<uml_Property> uml_propertys;


    public uml_StructuredClassifier(
    ) {
        super(
        );
        this.uml_propertys = new ArrayList<>();
    }

    public uml_StructuredClassifier(
        ArrayList<uml_Property> uml_propertys    ) {
        this.uml_propertys = uml_propertys;
    }


    public List<uml_Property> getUml_propertys() {
        return uml_propertys;
    }

    public void addUml_property(Uml_property uml_property) {
        this.uml_propertys.add(uml_property);
    }

}