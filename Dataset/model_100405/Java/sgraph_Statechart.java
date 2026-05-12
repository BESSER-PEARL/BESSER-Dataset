





import java.util.List;
import java.util.ArrayList;

public class sgraph_Statechart extends DocumentedElement, CompositeElement, ReactiveElement, ScopedElement, SpecificationElement, NamedElement {

    private String domainID;



    public sgraph_Statechart(
        String domainID    ) {
        super(
        );
        this.domainID = domainID;
    }


    public String getDomainid() {
        return domainID;
    }

    public void setDomainid(String domainID) {
        this.domainID = domainID;
    }


}