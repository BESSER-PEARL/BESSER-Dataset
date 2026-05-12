





import java.util.List;
import java.util.ArrayList;

public class umluseCases_Element extends EModelElement {






    private List<umluseCases_Element> umlusecases_elements;




    private umluseCases_Element umlusecases_element;


    public umluseCases_Element(
    ) {
        super(
        );
        this.umlusecases_elements = new ArrayList<>();
    }

    public umluseCases_Element(
        ArrayList<umluseCases_Element> umlusecases_elements    ) {
        this.umlusecases_elements = umlusecases_elements;
    }


    public List<umluseCases_Element> getUmlusecases_elements() {
        return umlusecases_elements;
    }

    public void addUmlusecases_element(Umlusecases_element umlusecases_element) {
        this.umlusecases_elements.add(umlusecases_element);
    }
    public umluseCases_Element getUmlusecases_element() {
        return umlusecases_element;
    }

    public void setUmlusecases_element(umluseCases_Element umlusecases_element) {
        this.umlusecases_element = umlusecases_element;
    }

}