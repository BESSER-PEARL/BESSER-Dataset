





import java.util.List;
import java.util.ArrayList;

public class simulink_SimulinkReference  {

    private String name;
    private String qualifier;





    private simulink_SimulinkElement simulink_simulinkelement;


    public simulink_SimulinkReference(
        String name,        String qualifier    ) {
        this.name = name;
        this.qualifier = qualifier;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getQualifier() {
        return qualifier;
    }

    public void setQualifier(String qualifier) {
        this.qualifier = qualifier;
    }

    public simulink_SimulinkElement getSimulink_simulinkelement() {
        return simulink_simulinkelement;
    }

    public void setSimulink_simulinkelement(simulink_SimulinkElement simulink_simulinkelement) {
        this.simulink_simulinkelement = simulink_simulinkelement;
    }

}