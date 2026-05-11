





import java.util.List;
import java.util.ArrayList;

public class diagram_description_EdgeMapping extends description_DiagramElementMapping, description_DocumentedElement, description_IEdgeMapping {

    private String domainClass;
    private boolean useDomainElement;
    private String targetFinderExpression;
    private String sourceFinderExpression;
    private String pathExpression;
    private String targetExpression;



    public diagram_description_EdgeMapping(
        String domainClass,        boolean useDomainElement,        String targetFinderExpression,        String sourceFinderExpression,        String pathExpression,        String targetExpression    ) {
        super(
        );
        this.domainClass = domainClass;
        this.useDomainElement = useDomainElement;
        this.targetFinderExpression = targetFinderExpression;
        this.sourceFinderExpression = sourceFinderExpression;
        this.pathExpression = pathExpression;
        this.targetExpression = targetExpression;
    }


    public String getDomainclass() {
        return domainClass;
    }

    public void setDomainclass(String domainClass) {
        this.domainClass = domainClass;
    }
    public boolean getUsedomainelement() {
        return useDomainElement;
    }

    public void setUsedomainelement(boolean useDomainElement) {
        this.useDomainElement = useDomainElement;
    }
    public String getTargetfinderexpression() {
        return targetFinderExpression;
    }

    public void setTargetfinderexpression(String targetFinderExpression) {
        this.targetFinderExpression = targetFinderExpression;
    }
    public String getSourcefinderexpression() {
        return sourceFinderExpression;
    }

    public void setSourcefinderexpression(String sourceFinderExpression) {
        this.sourceFinderExpression = sourceFinderExpression;
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


}