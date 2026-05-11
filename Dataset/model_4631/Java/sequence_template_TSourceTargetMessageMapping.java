





import java.util.List;
import java.util.ArrayList;

public class sequence_template_TSourceTargetMessageMapping extends TMessageMapping {

    private String targetFinderExpression;
    private String sourceFinderExpression;
    private boolean useDomainElement;



    public sequence_template_TSourceTargetMessageMapping(
        String targetFinderExpression,        String sourceFinderExpression,        boolean useDomainElement    ) {
        super(
        );
        this.targetFinderExpression = targetFinderExpression;
        this.sourceFinderExpression = sourceFinderExpression;
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
    public boolean getUsedomainelement() {
        return useDomainElement;
    }

    public void setUsedomainelement(boolean useDomainElement) {
        this.useDomainElement = useDomainElement;
    }


}