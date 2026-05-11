





import java.util.List;
import java.util.ArrayList;

public class model_Chart extends Widget, SkinSupport {

    private String chartType;



    public model_Chart(
        String chartType    ) {
        super(
        );
        this.chartType = chartType;
    }


    public String getCharttype() {
        return chartType;
    }

    public void setCharttype(String chartType) {
        this.chartType = chartType;
    }


}