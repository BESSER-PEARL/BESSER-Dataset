





import java.util.List;
import java.util.ArrayList;

public class model_values_FunctionPlot  {

    private String stepValue;
    private String initialValue;
    private String xAxisLabel;
    private String finalValue;
    private String title;
    private String yAxisLabel;



    public model_values_FunctionPlot(
        String stepValue,        String initialValue,        String xAxisLabel,        String finalValue,        String title,        String yAxisLabel    ) {
        this.stepValue = stepValue;
        this.initialValue = initialValue;
        this.xAxisLabel = xAxisLabel;
        this.finalValue = finalValue;
        this.title = title;
        this.yAxisLabel = yAxisLabel;
    }


    public String getStepvalue() {
        return stepValue;
    }

    public void setStepvalue(String stepValue) {
        this.stepValue = stepValue;
    }
    public String getInitialvalue() {
        return initialValue;
    }

    public void setInitialvalue(String initialValue) {
        this.initialValue = initialValue;
    }
    public String getXaxislabel() {
        return xAxisLabel;
    }

    public void setXaxislabel(String xAxisLabel) {
        this.xAxisLabel = xAxisLabel;
    }
    public String getFinalvalue() {
        return finalValue;
    }

    public void setFinalvalue(String finalValue) {
        this.finalValue = finalValue;
    }
    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }
    public String getYaxislabel() {
        return yAxisLabel;
    }

    public void setYaxislabel(String yAxisLabel) {
        this.yAxisLabel = yAxisLabel;
    }


}