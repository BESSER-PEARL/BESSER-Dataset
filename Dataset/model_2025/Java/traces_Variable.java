





import java.util.List;
import java.util.ArrayList;

public class traces_Variable  {

    private String name;





    private traces_Value traces_value;




    private List<traces_Value> traces_values;




    private traces_SimulatorRun traces_simulatorrun;




    private traces_SimulatorRun traces_simulatorrun;


    public traces_Variable(
        String name    ) {
        this.name = name;
        this.traces_values = new ArrayList<>();
    }

    public traces_Variable(
        String name        ArrayList<traces_Value> traces_values    ) {
        this.name = name;
        this.traces_values = traces_values;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public traces_Value getTraces_value() {
        return traces_value;
    }

    public void setTraces_value(traces_Value traces_value) {
        this.traces_value = traces_value;
    }
    public List<traces_Value> getTraces_values() {
        return traces_values;
    }

    public void addTraces_value(Traces_value traces_value) {
        this.traces_values.add(traces_value);
    }
    public traces_SimulatorRun getTraces_simulatorrun() {
        return traces_simulatorrun;
    }

    public void setTraces_simulatorrun(traces_SimulatorRun traces_simulatorrun) {
        this.traces_simulatorrun = traces_simulatorrun;
    }
    public traces_SimulatorRun getTraces_simulatorrun() {
        return traces_simulatorrun;
    }

    public void setTraces_simulatorrun(traces_SimulatorRun traces_simulatorrun) {
        this.traces_simulatorrun = traces_simulatorrun;
    }

}