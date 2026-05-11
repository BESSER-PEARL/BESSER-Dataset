





import java.util.List;
import java.util.ArrayList;

public class diagram_description_EdgeMapping extends description_DiagramElementMapping, description_DocumentedElement, description_IEdgeMapping {

    private boolean useDomainElement;
    private String domainClass;
    private String targetFinderExpression;
    private String sourceFinderExpression;
    private String targetExpression;
    private String pathExpression;



    public diagram_description_EdgeMapping(
        boolean useDomainElement,        String domainClass,        String targetFinderExpression,        String sourceFinderExpression,        String targetExpression,        String pathExpression    ) {
        super(
        );
        this.useDomainElement = useDomainElement;
        this.domainClass = domainClass;
        this.targetFinderExpression = targetFinderExpression;
        this.sourceFinderExpression = sourceFinderExpression;
        this.targetExpression = targetExpression;
        this.pathExpression = pathExpression;
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
    public String getTargetexpression() {
        return targetExpression;
    }

    public void setTargetexpression(String targetExpression) {
        this.targetExpression = targetExpression;
    }
    public String getPathexpression() {
        return pathExpression;
    }

    public void setPathexpression(String pathExpression) {
        this.pathExpression = pathExpression;
    }


}