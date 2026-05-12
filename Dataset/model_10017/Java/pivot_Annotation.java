





import java.util.List;
import java.util.ArrayList;

public class pivot_Annotation extends NamedElement {






    private List<pivot_Element> pivot_elements;




    private List<pivot_Detail> pivot_details;




    private List<pivot_Element> pivot_elements;


    public pivot_Annotation(
    ) {
        super(
        );
        this.pivot_elements = new ArrayList<>();
        this.pivot_details = new ArrayList<>();
        this.pivot_elements = new ArrayList<>();
    }

    public pivot_Annotation(
        ArrayList<pivot_Element> pivot_elements,        ArrayList<pivot_Detail> pivot_details,        ArrayList<pivot_Element> pivot_elements    ) {
        this.pivot_elements = pivot_elements;
        this.pivot_details = pivot_details;
        this.pivot_elements = pivot_elements;
    }


    public List<pivot_Element> getPivot_elements() {
        return pivot_elements;
    }

    public void addPivot_element(Pivot_element pivot_element) {
        this.pivot_elements.add(pivot_element);
    }
    public List<pivot_Detail> getPivot_details() {
        return pivot_details;
    }

    public void addPivot_detail(Pivot_detail pivot_detail) {
        this.pivot_details.add(pivot_detail);
    }
    public List<pivot_Element> getPivot_elements() {
        return pivot_elements;
    }

    public void addPivot_element(Pivot_element pivot_element) {
        this.pivot_elements.add(pivot_element);
    }

}