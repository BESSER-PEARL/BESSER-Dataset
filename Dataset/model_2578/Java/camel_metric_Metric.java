





import java.util.List;
import java.util.ArrayList;

public class camel_metric_Metric extends MetricFormulaParameter {

    private String layer;
    private String valueDirection;
    private String description;
    private boolean isVariable;



    public camel_metric_Metric(
        String layer,        String valueDirection,        String description,        boolean isVariable    ) {
        super(
        );
        this.layer = layer;
        this.valueDirection = valueDirection;
        this.description = description;
        this.isVariable = isVariable;
    }


    public String getLayer() {
        return layer;
    }

    public void setLayer(String layer) {
        this.layer = layer;
    }
    public String getValuedirection() {
        return valueDirection;
    }

    public void setValuedirection(String valueDirection) {
        this.valueDirection = valueDirection;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public boolean getIsvariable() {
        return isVariable;
    }

    public void setIsvariable(boolean isVariable) {
        this.isVariable = isVariable;
    }


}