





import java.util.List;
import java.util.ArrayList;

public class metric_ConstraintMetric extends Metric {

    private String usedIterators;
    private String calledProperties;
    private int numberOfLetExpressions;
    private int numberOfIfExpressions;
    private String usedLiterals;
    private String calledOperations;
    private int expressionCount;
    private int expressionDepth;





    private metric_ConstraintMetrics metric_constraintmetrics;


    public metric_ConstraintMetric(
        String usedIterators,        String calledProperties,        int numberOfLetExpressions,        int numberOfIfExpressions,        String usedLiterals,        String calledOperations,        int expressionCount,        int expressionDepth    ) {
        super(
        );
        this.usedIterators = usedIterators;
        this.calledProperties = calledProperties;
        this.numberOfLetExpressions = numberOfLetExpressions;
        this.numberOfIfExpressions = numberOfIfExpressions;
        this.usedLiterals = usedLiterals;
        this.calledOperations = calledOperations;
        this.expressionCount = expressionCount;
        this.expressionDepth = expressionDepth;
    }


    public String getUsediterators() {
        return usedIterators;
    }

    public void setUsediterators(String usedIterators) {
        this.usedIterators = usedIterators;
    }
    public String getCalledproperties() {
        return calledProperties;
    }

    public void setCalledproperties(String calledProperties) {
        this.calledProperties = calledProperties;
    }
    public int getNumberofletexpressions() {
        return numberOfLetExpressions;
    }

    public void setNumberofletexpressions(int numberOfLetExpressions) {
        this.numberOfLetExpressions = numberOfLetExpressions;
    }
    public int getNumberofifexpressions() {
        return numberOfIfExpressions;
    }

    public void setNumberofifexpressions(int numberOfIfExpressions) {
        this.numberOfIfExpressions = numberOfIfExpressions;
    }
    public String getUsedliterals() {
        return usedLiterals;
    }

    public void setUsedliterals(String usedLiterals) {
        this.usedLiterals = usedLiterals;
    }
    public String getCalledoperations() {
        return calledOperations;
    }

    public void setCalledoperations(String calledOperations) {
        this.calledOperations = calledOperations;
    }
    public int getExpressioncount() {
        return expressionCount;
    }

    public void setExpressioncount(int expressionCount) {
        this.expressionCount = expressionCount;
    }
    public int getExpressiondepth() {
        return expressionDepth;
    }

    public void setExpressiondepth(int expressionDepth) {
        this.expressionDepth = expressionDepth;
    }

    public metric_ConstraintMetrics getMetric_constraintmetrics() {
        return metric_constraintmetrics;
    }

    public void setMetric_constraintmetrics(metric_ConstraintMetrics metric_constraintmetrics) {
        this.metric_constraintmetrics = metric_constraintmetrics;
    }

}