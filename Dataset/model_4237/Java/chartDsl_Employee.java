





import java.util.List;
import java.util.ArrayList;

public class chartDsl_Employee  {

    private String name;





    private chartDsl_Company chartdsl_company;


    public chartDsl_Employee(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public chartDsl_Company getChartdsl_company() {
        return chartdsl_company;
    }

    public void setChartdsl_company(chartDsl_Company chartdsl_company) {
        this.chartdsl_company = chartdsl_company;
    }

}