





import java.util.List;
import java.util.ArrayList;

public class model_values_FunctionPlot  {

    private String xAxisLabel;
    private String finalValue;
    private String stepValue;
    private String yAxisLabel;
    private String title;
    private String initialValue;



    public model_values_FunctionPlot(
        String xAxisLabel,        String finalValue,        String stepValue,        String yAxisLabel,        String title,        String initialValue    ) {
        this.xAxisLabel = xAxisLabel;
        this.finalValue = finalValue;
        this.stepValue = stepValue;
        this.yAxisLabel = yAxisLabel;
        this.title = title;
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
    public String getStepvalue() {
        return stepValue;
    }

    public void setStepvalue(String stepValue) {
        this.stepValue = stepValue;
    }
    public String getYaxislabel() {
        return yAxisLabel;
    }

    public void setYaxislabel(String yAxisLabel) {
        this.yAxisLabel = yAxisLabel;
    }
    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }
    public String getInitialvalue() {
        return initialValue;
    }

    public void setInitialvalue(String initialValue) {
        this.initialValue = initialValue;
    }


}