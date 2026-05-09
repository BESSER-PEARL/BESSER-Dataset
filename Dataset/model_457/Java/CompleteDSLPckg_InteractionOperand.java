





import java.util.List;
import java.util.ArrayList;

public class CompleteDSLPckg_InteractionOperand extends Namespace {






    private List<CompleteDSLPckg_InteractionFragment> completedslpckg_interactionfragments;




    private CompleteDSLPckg_InteractionFragment completedslpckg_interactionfragment;


    public CompleteDSLPckg_InteractionOperand(
    ) {
        super(
        );
        this.completedslpckg_interactionfragments = new ArrayList<>();
    }

    public CompleteDSLPckg_InteractionOperand(
        ArrayList<CompleteDSLPckg_InteractionFragment> completedslpckg_interactionfragments    ) {
        this.completedslpckg_interactionfragments = completedslpckg_interactionfragments;
    }


    public List<CompleteDSLPckg_InteractionFragment> getCompletedslpckg_interactionfragments() {
        return completedslpckg_interactionfragments;
    }

    public void addCompletedslpckg_interactionfragment(Completedslpckg_interactionfragment completedslpckg_interactionfragment) {
        this.completedslpckg_interactionfragments.add(completedslpckg_interactionfragment);
    }
    public CompleteDSLPckg_InteractionFragment getCompletedslpckg_interactionfragment() {
        return completedslpckg_interactionfragment;
    }

    public void setCompletedslpckg_interactionfragment(CompleteDSLPckg_InteractionFragment completedslpckg_interactionfragment) {
        this.completedslpckg_interactionfragment = completedslpckg_interactionfragment;
    }

}