





import java.util.List;
import java.util.ArrayList;

public class metric_ConstraintMetric extends Metric {

    private String calledProperties;
    private int expressionCount;
    private String usedLiterals;
    private int numberOfLetExpressions;
    private int numberOfIfExpressions;
    private String usedIterators;
    private String calledOperations;
    private int expressionDepth;



    public metric_ConstraintMetric(
        String calledProperties,        int expressionCount,        String usedLiterals,        int numberOfLetExpressions,        int numberOfIfExpressions,        String usedIterators,        String calledOperations,        int expressionDepth    ) {
        super(
        );
        this.calledProperties = calledProperties;
        this.expressionCount = expressionCount;
        this.usedLiterals = usedLiterals;
        this.numberOfLetExpressions = numberOfLetExpressions;
        this.numberOfIfExpressions = numberOfIfExpressions;
        this.usedIterators = usedIterators;
        this.calledOperations = calledOperations;
        this.expressionDepth = expressionDepth;
    }


    public String getCalledproperties() {
        return calledProperties;
    }

    public void setCalledproperties(String calledProperties) {
        this.calledProperties = calledProperties;
    }
    public int getExpressioncount() {
        return expressionCount;
    }

    public void setExpressioncount(int expressionCount) {
        this.expressionCount = expressionCount;
    }
    public String getUsedliterals() {
        return usedLiterals;
    }

    public void setUsedliterals(String usedLiterals) {
        this.usedLiterals = usedLiterals;
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
    public String getUsediterators() {
        return usedIterators;
    }

    public void setUsediterators(String usedIterators) {
        this.usedIterators = usedIterators;
    }
    public String getCalledoperations() {
        return calledOperations;
    }

    public void setCalledoperations(String calledOperations) {
        this.calledOperations = calledOperations;
    }
    public int getExpressiondepth() {
        return expressionDepth;
    }

    public void setExpressiondepth(int expressionDepth) {
        this.expressionDepth = expressionDepth;
    }


}