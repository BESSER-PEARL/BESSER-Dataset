





import java.util.List;
import java.util.ArrayList;

public class uma_FulfillableElement extends DescribableElement {






    private List<uma_FulfillableElement> uma_fulfillableelements;


    public uma_FulfillableElement(
    ) {
        super(
        );
        this.uma_fulfillableelements = new ArrayList<>();
    }

    public uma_FulfillableElement(
        ArrayList<uma_FulfillableElement> uma_fulfillableelements    ) {
        this.uma_fulfillableelements = uma_fulfillableelements;
    }


    public List<uma_FulfillableElement> getUma_fulfillableelements() {
        return uma_fulfillableelements;
    }

    public void addUma_fulfillableelement(Uma_fulfillableelement uma_fulfillableelement) {
        this.uma_fulfillableelements.add(uma_fulfillableelement);
    }

}