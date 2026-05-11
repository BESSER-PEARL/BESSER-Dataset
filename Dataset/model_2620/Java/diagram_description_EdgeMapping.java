





import java.util.List;
import java.util.ArrayList;

public class diagram_description_EdgeMapping extends description_DiagramElementMapping, description_IEdgeMapping, description_DocumentedElement {

    private String sourceFinderExpression;
    private boolean useDomainElement;
    private String pathExpression;
    private String targetExpression;
    private String domainClass;
    private String targetFinderExpression;



    public diagram_description_EdgeMapping(
        String sourceFinderExpression,        boolean useDomainElement,        String pathExpression,        String targetExpression,        String domainClass,        String targetFinderExpression    ) {
        super(
        );
        this.sourceFinderExpression = sourceFinderExpression;
        this.useDomainElement = useDomainElement;
        this.pathExpression = pathExpression;
        this.targetExpression = targetExpression;
        this.domainClass = domainClass;
        this.targetFinderExpression = targetFinderExpression;
    }


    public String getSourcefinderexpression() {
        return sourceFinderExpression;
    }

    public void setSourcefinderexpression(String sourceFinderExpression) {
        this.sourceFinderExpression = sourceFinderExpression;
    }
    public boolean getUsedomainelement() {
        return useDomainElement;
    }

    public void setUsedomainelement(boolean useDomainElement) {
        this.useDomainElement = useDomainElement;
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


}