





import java.util.List;
import java.util.ArrayList;

public class uml3_0_0_StructuredClassifier extends Classifier {






    private List<uml3_0_0_ConnectableElement> uml3_0_0_connectableelements;


    public uml3_0_0_StructuredClassifier(
    ) {
        super(
        );
        this.uml3_0_0_connectableelements = new ArrayList<>();
    }

    public uml3_0_0_StructuredClassifier(
        ArrayList<uml3_0_0_ConnectableElement> uml3_0_0_connectableelements    ) {
        this.uml3_0_0_connectableelements = uml3_0_0_connectableelements;
    }


    public List<uml3_0_0_ConnectableElement> getUml3_0_0_connectableelements() {
        return uml3_0_0_connectableelements;
    }

    public void addUml3_0_0_connectableelement(Uml3_0_0_connectableelement uml3_0_0_connectableelement) {
        this.uml3_0_0_connectableelements.add(uml3_0_0_connectableelement);
    }

}