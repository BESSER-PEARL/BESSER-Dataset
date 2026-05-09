





import java.util.List;
import java.util.ArrayList;

public class CompleteDSLPckg_InteractionUse extends InteractionFragment {






    private CompleteDSLPckg_ValueSpecification completedslpckg_valuespecification;




    private CompleteDSLPckg_Property completedslpckg_property;




    private List<CompleteDSLPckg_ValueSpecification> completedslpckg_valuespecifications;




    private List<CompleteDSLPckg_Gate> completedslpckg_gates;


    public CompleteDSLPckg_InteractionUse(
    ) {
        super(
        );
        this.completedslpckg_valuespecifications = new ArrayList<>();
        this.completedslpckg_gates = new ArrayList<>();
    }

    public CompleteDSLPckg_InteractionUse(
        ArrayList<CompleteDSLPckg_ValueSpecification> completedslpckg_valuespecifications,        ArrayList<CompleteDSLPckg_Gate> completedslpckg_gates    ) {
        this.completedslpckg_valuespecifications = completedslpckg_valuespecifications;
        this.completedslpckg_gates = completedslpckg_gates;
    }


    public CompleteDSLPckg_ValueSpecification getCompletedslpckg_valuespecification() {
        return completedslpckg_valuespecification;
    }

    public void setCompletedslpckg_valuespecification(CompleteDSLPckg_ValueSpecification completedslpckg_valuespecification) {
        this.completedslpckg_valuespecification = completedslpckg_valuespecification;
    }
    public CompleteDSLPckg_Property getCompletedslpckg_property() {
        return completedslpckg_property;
    }

    public void setCompletedslpckg_property(CompleteDSLPckg_Property completedslpckg_property) {
        this.completedslpckg_property = completedslpckg_property;
    }
    public List<CompleteDSLPckg_ValueSpecification> getCompletedslpckg_valuespecifications() {
        return completedslpckg_valuespecifications;
    }

    public void addCompletedslpckg_valuespecification(Completedslpckg_valuespecification completedslpckg_valuespecification) {
        this.completedslpckg_valuespecifications.add(completedslpckg_valuespecification);
    }
    public List<CompleteDSLPckg_Gate> getCompletedslpckg_gates() {
        return completedslpckg_gates;
    }

    public void addCompletedslpckg_gate(Completedslpckg_gate completedslpckg_gate) {
        this.completedslpckg_gates.add(completedslpckg_gate);
    }

}