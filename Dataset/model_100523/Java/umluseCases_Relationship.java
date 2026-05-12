





import java.util.List;
import java.util.ArrayList;

public class umluseCases_Relationship extends Element {






    private List<umluseCases_Element> umlusecases_elements;


    public umluseCases_Relationship(
    ) {
        super(
        );
        this.umlusecases_elements = new ArrayList<>();
    }

    public umluseCases_Relationship(
        ArrayList<umluseCases_Element> umlusecases_elements    ) {
        this.umlusecases_elements = umlusecases_elements;
    }


    public List<umluseCases_Element> getUmlusecases_elements() {
        return umlusecases_elements;
    }

    public void addUmlusecases_element(Umlusecases_element umlusecases_element) {
        this.umlusecases_elements.add(umlusecases_element);
    }

}