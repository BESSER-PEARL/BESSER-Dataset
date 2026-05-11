





import java.util.List;
import java.util.ArrayList;

public class chartDsl_Task  {

    private String name;





    private chartDsl_Employee chartdsl_employee;




    private chartDsl_Project chartdsl_project;


    public chartDsl_Task(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public chartDsl_Employee getChartdsl_employee() {
        return chartdsl_employee;
    }

    public void setChartdsl_employee(chartDsl_Employee chartdsl_employee) {
        this.chartdsl_employee = chartdsl_employee;
    }
    public chartDsl_Project getChartdsl_project() {
        return chartdsl_project;
    }

    public void setChartdsl_project(chartDsl_Project chartdsl_project) {
        this.chartdsl_project = chartdsl_project;
    }

}