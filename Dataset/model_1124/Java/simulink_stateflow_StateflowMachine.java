





import java.util.List;
import java.util.ArrayList;

public class simulink_stateflow_StateflowMachine extends StateflowElement {






    private List<Chart> charts;


    public simulink_stateflow_StateflowMachine(
    ) {
        super(
        );
        this.charts = new ArrayList<>();
    }

    public simulink_stateflow_StateflowMachine(
        ArrayList<Chart> charts    ) {
        this.charts = charts;
    }


    public List<Chart> getCharts() {
        return charts;
    }

    public void addChart(Chart chart) {
        this.charts.add(chart);
    }

}