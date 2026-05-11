





import java.util.List;
import java.util.ArrayList;

public class viewpoint_description_EdgeMapping extends description_IEdgeMapping, description_DocumentedElement, description_DiagramElementMapping {

    private String targetFinderExpression;
    private String pathExpression;
    private String targetExpression;
    private boolean useDomainElement;
    private String domainClass;
    private String sourceFinderExpression;



    public viewpoint_description_EdgeMapping(
        String targetFinderExpression,        String pathExpression,        String targetExpression,        boolean useDomainElement,        String domainClass,        String sourceFinderExpression    ) {
        super(
        );
        this.targetFinderExpression = targetFinderExpression;
        this.pathExpression = pathExpression;
        this.targetExpression = targetExpression;
        this.useDomainElement = useDomainElement;
        this.domainClass = domainClass;
        this.sourceFinderExpression = sourceFinderExpression;
    }


    public String getTargetfinderexpression() {
        return targetFinderExpression;
    }

    public void setTargetfinderexpression(String targetFinderExpression) {
        this.targetFinderExpression = targetFinderExpression;
    }
    public String getPathexpression() {
        return pathExpression;
    }

    public void setPathexpression(String pathExpression) {
        this.pathExpression = pathExpression;
    }
    public String getTargetexpression() {
        return targetExpression;
    }

    public void setTargetexpression(String targetExpression) {
        this.targetExpression = targetExpression;
    }
    public boolean getUsedomainelement() {
        return useDomainElement;
    }

    public void setUsedomainelement(boolean useDomainElement) {
        this.useDomainElement = useDomainElement;
    }
    public String getDomainclass() {
        return domainClass;
    }

    public void setDomainclass(String domainClass) {
        this.domainClass = domainClass;
    }
    public String getSourcefinderexpression() {
        return sourceFinderExpression;
    }

    public void setSourcefinderexpression(String sourceFinderExpression) {
        this.sourceFinderExpression = sourceFinderExpression;
    }


}