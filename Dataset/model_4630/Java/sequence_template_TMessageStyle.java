





import java.util.List;
import java.util.ArrayList;

public class sequence_template_TMessageStyle extends TTransformer {

    private String lineStyle;
    private String labelExpression;
    private String sourceArrow;
    private String targetArrow;



    public sequence_template_TMessageStyle(
        String lineStyle,        String labelExpression,        String sourceArrow,        String targetArrow    ) {
        super(
        );
        this.lineStyle = lineStyle;
        this.labelExpression = labelExpression;
        this.sourceArrow = sourceArrow;
        this.targetArrow = targetArrow;
    }


    public String getLinestyle() {
        return lineStyle;
    }

    public void setLinestyle(String lineStyle) {
        this.lineStyle = lineStyle;
    }
    public String getLabelexpression() {
        return labelExpression;
    }

    public void setLabelexpression(String labelExpression) {
        this.labelExpression = labelExpression;
    }
    public String getSourcearrow() {
        return sourceArrow;
    }

    public void setSourcearrow(String sourceArrow) {
        this.sourceArrow = sourceArrow;
    }
    public String getTargetarrow() {
        return targetArrow;
    }

    public void setTargetarrow(String targetArrow) {
        this.targetArrow = targetArrow;
    }


}