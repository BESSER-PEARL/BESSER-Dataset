





import java.util.List;
import java.util.ArrayList;

public class diagram_description_EdgeMapping extends description_IEdgeMapping, description_DiagramElementMapping, description_DocumentedElement {

    private String targetExpression;
    private String targetFinderExpression;
    private boolean useDomainElement;
    private String domainClass;
    private String sourceFinderExpression;
    private String pathExpression;



    public diagram_description_EdgeMapping(
        String targetExpression,        String targetFinderExpression,        boolean useDomainElement,        String domainClass,        String sourceFinderExpression,        String pathExpression    ) {
        super(
        );
        this.targetExpression = targetExpression;
        this.targetFinderExpression = targetFinderExpression;
        this.useDomainElement = useDomainElement;
        this.domainClass = domainClass;
        this.sourceFinderExpression = sourceFinderExpression;
        this.pathExpression = pathExpression;
    }


    public String getTargetexpression() {
        return targetExpression;
    }

    public void setTargetexpression(String targetExpression) {
        this.targetExpression = targetExpression;
    }
    public String getTargetfinderexpression() {
        return targetFinderExpression;
    }

    public void setTargetfinderexpression(String targetFinderExpression) {
        this.targetFinderExpression = targetFinderExpression;
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
    public String getPathexpression() {
        return pathExpression;
    }

    public void setPathexpression(String pathExpression) {
        this.pathExpression = pathExpression;
    }


}