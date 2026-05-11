





import java.util.List;
import java.util.ArrayList;

public class sequence_template_TSequenceDiagram extends description_RepresentationTemplate, template_TTransformer {

    private String endsOrdering;
    private String domainClass;



    public sequence_template_TSequenceDiagram(
        String endsOrdering,        String domainClass    ) {
        super(
        );
        this.endsOrdering = endsOrdering;
        this.domainClass = domainClass;
    }


    public String getEndsordering() {
        return endsOrdering;
    }

    public void setEndsordering(String endsOrdering) {
        this.endsOrdering = endsOrdering;
    }
    public String getDomainclass() {
        return domainClass;
    }

    public void setDomainclass(String domainClass) {
        this.domainClass = domainClass;
    }


}