





import java.util.List;
import java.util.ArrayList;

public class simulink_BusSignalMapping  {

    private String mappingPath;
    private boolean incomplete;





    private simulink_BusSelector simulink_busselector;




    private simulink_OutPort simulink_outport;




    private simulink_OutPort simulink_outport;




    private simulink_BusSelector simulink_busselector;


    public simulink_BusSignalMapping(
        String mappingPath,        boolean incomplete    ) {
        this.mappingPath = mappingPath;
        this.incomplete = incomplete;
    }


    public String getMappingpath() {
        return mappingPath;
    }

    public void setMappingpath(String mappingPath) {
        this.mappingPath = mappingPath;
    }
    public boolean getIncomplete() {
        return incomplete;
    }

    public void setIncomplete(boolean incomplete) {
        this.incomplete = incomplete;
    }

    public simulink_BusSelector getSimulink_busselector() {
        return simulink_busselector;
    }

    public void setSimulink_busselector(simulink_BusSelector simulink_busselector) {
        this.simulink_busselector = simulink_busselector;
    }
    public simulink_OutPort getSimulink_outport() {
        return simulink_outport;
    }

    public void setSimulink_outport(simulink_OutPort simulink_outport) {
        this.simulink_outport = simulink_outport;
    }
    public simulink_OutPort getSimulink_outport() {
        return simulink_outport;
    }

    public void setSimulink_outport(simulink_OutPort simulink_outport) {
        this.simulink_outport = simulink_outport;
    }
    public simulink_BusSelector getSimulink_busselector() {
        return simulink_busselector;
    }

    public void setSimulink_busselector(simulink_BusSelector simulink_busselector) {
        this.simulink_busselector = simulink_busselector;
    }

}