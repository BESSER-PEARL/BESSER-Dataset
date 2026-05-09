





import java.util.List;
import java.util.ArrayList;

public class uml_StructuredClassifier extends Classifier {






    private List<uml_ConnectableElement> uml_connectableelements;


    public uml_StructuredClassifier(
    ) {
        super(
        );
        this.uml_connectableelements = new ArrayList<>();
    }

    public uml_StructuredClassifier(
        ArrayList<uml_ConnectableElement> uml_connectableelements    ) {
        this.uml_connectableelements = uml_connectableelements;
    }


    public List<uml_ConnectableElement> getUml_connectableelements() {
        return uml_connectableelements;
    }

    public void addUml_connectableelement(Uml_connectableelement uml_connectableelement) {
        this.uml_connectableelements.add(uml_connectableelement);
    }

}