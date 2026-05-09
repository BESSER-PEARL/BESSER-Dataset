





import java.util.List;
import java.util.ArrayList;

public class model_values_FunctionPlot  {

    private String finalValue;
    private String title;
    private String xAxisLabel;
    private String initialValue;
    private String yAxisLabel;
    private String stepValue;



    public model_values_FunctionPlot(
        String finalValue,        String title,        String xAxisLabel,        String initialValue,        String yAxisLabel,        String stepValue    ) {
        this.finalValue = finalValue;
        this.title = title;
        this.xAxisLabel = xAxisLabel;
        this.initialValue = initialValue;
        this.yAxisLabel = yAxisLabel;
        this.stepValue = stepValue;
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
    public String getXaxislabel() {
        return xAxisLabel;
    }

    public void setXaxislabel(String xAxisLabel) {
        this.xAxisLabel = xAxisLabel;
    }
    public String getInitialvalue() {
        return initialValue;
    }

    public void setInitialvalue(String initialValue) {
        this.initialValue = initialValue;
    }
    public String getYaxislabel() {
        return yAxisLabel;
    }

    public void setYaxislabel(String yAxisLabel) {
        this.yAxisLabel = yAxisLabel;
    }
    public String getStepvalue() {
        return stepValue;
    }

    public void setStepvalue(String stepValue) {
        this.stepValue = stepValue;
    }


}