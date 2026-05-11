





import java.util.List;
import java.util.ArrayList;

public class chartDsl_Project  {

    private String projectType;
    private String name;





    private chartDsl_Company chartdsl_company;


    public chartDsl_Project(
        String projectType,        String name    ) {
        this.projectType = projectType;
        this.name = name;
    }


    public String getProjecttype() {
        return projectType;
    }

    public void setProjecttype(String projectType) {
        this.projectType = projectType;
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