





import java.util.List;
import java.util.ArrayList;

public class UMLModel_InteractionOperand extends Namespace, InteractionFragment {






    private List<UMLModel_InteractionFragment> umlmodel_interactionfragments;


    public UMLModel_InteractionOperand(
    ) {
        super(
        );
        this.umlmodel_interactionfragments = new ArrayList<>();
    }

    public UMLModel_InteractionOperand(
        ArrayList<UMLModel_InteractionFragment> umlmodel_interactionfragments    ) {
        this.umlmodel_interactionfragments = umlmodel_interactionfragments;
    }


    public List<UMLModel_InteractionFragment> getUmlmodel_interactionfragments() {
        return umlmodel_interactionfragments;
    }

    public void addUmlmodel_interactionfragment(Umlmodel_interactionfragment umlmodel_interactionfragment) {
        this.umlmodel_interactionfragments.add(umlmodel_interactionfragment);
    }

}