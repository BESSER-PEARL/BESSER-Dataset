





import java.util.List;
import java.util.ArrayList;

public class diagram_concern_ConcernDescription extends description_DocumentedElement, description_IdentifiedElement {






    private List<filter_FilterDescription> filter_filterdescriptions;


    public diagram_concern_ConcernDescription(
    ) {
        super(
        );
        this.filter_filterdescriptions = new ArrayList<>();
    }

    public diagram_concern_ConcernDescription(
        ArrayList<filter_FilterDescription> filter_filterdescriptions    ) {
        this.filter_filterdescriptions = filter_filterdescriptions;
    }


    public List<filter_FilterDescription> getFilter_filterdescriptions() {
        return filter_filterdescriptions;
    }

    public void addFilter_filterdescription(Filter_filterdescription filter_filterdescription) {
        this.filter_filterdescriptions.add(filter_filterdescription);
    }

}