





import java.util.List;
import java.util.ArrayList;

public class CompleteDSLPckg_Element  {






    private CompleteDSLPckg_Element completedslpckg_element;




    private List<CompleteDSLPckg_Element> completedslpckg_elements;


    public CompleteDSLPckg_Element(
    ) {
        this.completedslpckg_elements = new ArrayList<>();
    }

    public CompleteDSLPckg_Element(
        ArrayList<CompleteDSLPckg_Element> completedslpckg_elements    ) {
        this.completedslpckg_elements = completedslpckg_elements;
    }


    public CompleteDSLPckg_Element getCompletedslpckg_element() {
        return completedslpckg_element;
    }

    public void setCompletedslpckg_element(CompleteDSLPckg_Element completedslpckg_element) {
        this.completedslpckg_element = completedslpckg_element;
    }
    public List<CompleteDSLPckg_Element> getCompletedslpckg_elements() {
        return completedslpckg_elements;
    }

    public void addCompletedslpckg_element(Completedslpckg_element completedslpckg_element) {
        this.completedslpckg_elements.add(completedslpckg_element);
    }

}