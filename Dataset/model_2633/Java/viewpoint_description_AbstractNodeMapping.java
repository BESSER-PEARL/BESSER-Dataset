





import java.util.List;
import java.util.ArrayList;

public class viewpoint_description_AbstractNodeMapping extends description_DocumentedElement, description_DiagramElementMapping {

    private String domainClass;



    public viewpoint_description_AbstractNodeMapping(
        String domainClass    ) {
        super(
        );
        this.domainClass = domainClass;
    }


    public String getDomainclass() {
        return domainClass;
    }

    public void setDomainclass(String domainClass) {
        this.domainClass = domainClass;
    }


}