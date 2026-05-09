





import java.util.List;
import java.util.ArrayList;

public class CompleteDSLPckg_Relationship extends Element {






    private List<CompleteDSLPckg_Element> completedslpckg_elements;


    public CompleteDSLPckg_Relationship(
    ) {
        super(
        );
        this.completedslpckg_elements = new ArrayList<>();
    }

    public CompleteDSLPckg_Relationship(
        ArrayList<CompleteDSLPckg_Element> completedslpckg_elements    ) {
        this.completedslpckg_elements = completedslpckg_elements;
    }


    public List<CompleteDSLPckg_Element> getCompletedslpckg_elements() {
        return completedslpckg_elements;
    }

    public void addCompletedslpckg_element(Completedslpckg_element completedslpckg_element) {
        this.completedslpckg_elements.add(completedslpckg_element);
    }

}