





import java.util.List;
import java.util.ArrayList;

public class sequence_template_TSequenceDiagram extends template_TTransformer, description_RepresentationTemplate {

    private String domainClass;
    private String endsOrdering;



    public sequence_template_TSequenceDiagram(
        String domainClass,        String endsOrdering    ) {
        super(
        );
        this.domainClass = domainClass;
        this.endsOrdering = endsOrdering;
    }


    public String getDomainclass() {
        return domainClass;
    }

    public void setDomainclass(String domainClass) {
        this.domainClass = domainClass;
    }
    public String getEndsordering() {
        return endsOrdering;
    }

    public void setEndsordering(String endsOrdering) {
        this.endsOrdering = endsOrdering;
    }


}