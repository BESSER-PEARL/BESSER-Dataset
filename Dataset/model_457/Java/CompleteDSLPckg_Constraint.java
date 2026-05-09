





import java.util.List;
import java.util.ArrayList;

public class CompleteDSLPckg_Constraint extends PackageableElement {






    private CompleteDSLPckg_Namespace completedslpckg_namespace;




    private CompleteDSLPckg_ParameterSet completedslpckg_parameterset;




    private CompleteDSLPckg_Namespace completedslpckg_namespace;




    private CompleteDSLPckg_Extend completedslpckg_extend;




    private List<CompleteDSLPckg_Element> completedslpckg_elements;


    public CompleteDSLPckg_Constraint(
    ) {
        super(
        );
        this.completedslpckg_elements = new ArrayList<>();
    }

    public CompleteDSLPckg_Constraint(
        ArrayList<CompleteDSLPckg_Element> completedslpckg_elements    ) {
        this.completedslpckg_elements = completedslpckg_elements;
    }


    public CompleteDSLPckg_Namespace getCompletedslpckg_namespace() {
        return completedslpckg_namespace;
    }

    public void setCompletedslpckg_namespace(CompleteDSLPckg_Namespace completedslpckg_namespace) {
        this.completedslpckg_namespace = completedslpckg_namespace;
    }
    public CompleteDSLPckg_ParameterSet getCompletedslpckg_parameterset() {
        return completedslpckg_parameterset;
    }

    public void setCompletedslpckg_parameterset(CompleteDSLPckg_ParameterSet completedslpckg_parameterset) {
        this.completedslpckg_parameterset = completedslpckg_parameterset;
    }
    public CompleteDSLPckg_Namespace getCompletedslpckg_namespace() {
        return completedslpckg_namespace;
    }

    public void setCompletedslpckg_namespace(CompleteDSLPckg_Namespace completedslpckg_namespace) {
        this.completedslpckg_namespace = completedslpckg_namespace;
    }
    public CompleteDSLPckg_Extend getCompletedslpckg_extend() {
        return completedslpckg_extend;
    }

    public void setCompletedslpckg_extend(CompleteDSLPckg_Extend completedslpckg_extend) {
        this.completedslpckg_extend = completedslpckg_extend;
    }
    public List<CompleteDSLPckg_Element> getCompletedslpckg_elements() {
        return completedslpckg_elements;
    }

    public void addCompletedslpckg_element(Completedslpckg_element completedslpckg_element) {
        this.completedslpckg_elements.add(completedslpckg_element);
    }

}