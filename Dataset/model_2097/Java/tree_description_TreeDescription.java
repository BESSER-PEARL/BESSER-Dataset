





import java.util.List;
import java.util.ArrayList;

public class tree_description_TreeDescription extends description_RepresentationDescription, description_TreeItemMappingContainer {

    private String domainClass;
    private String preconditionExpression;



    public tree_description_TreeDescription(
        String domainClass,        String preconditionExpression    ) {
        super(
        );
        this.domainClass = domainClass;
        this.preconditionExpression = preconditionExpression;
    }


    public String getDomainclass() {
        return domainClass;
    }

    public void setDomainclass(String domainClass) {
        this.domainClass = domainClass;
    }
    public String getPreconditionexpression() {
        return preconditionExpression;
    }

    public void setPreconditionexpression(String preconditionExpression) {
        this.preconditionExpression = preconditionExpression;
    }


}