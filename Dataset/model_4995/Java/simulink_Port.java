





import java.util.List;
import java.util.ArrayList;

public class simulink_Port extends SimulinkElement {

    private int portNumber;
    private String dataType;





    private simulink_Block simulink_block;




    private simulink_Block simulink_block;


    public simulink_Port(
        int portNumber,        String dataType    ) {
        super(
        );
        this.portNumber = portNumber;
        this.dataType = dataType;
    }


    public int getPortnumber() {
        return portNumber;
    }

    public void setPortnumber(int portNumber) {
        this.portNumber = portNumber;
    }
    public String getDatatype() {
        return dataType;
    }

    public void setDatatype(String dataType) {
        this.dataType = dataType;
    }

    public simulink_Block getSimulink_block() {
        return simulink_block;
    }

    public void setSimulink_block(simulink_Block simulink_block) {
        this.simulink_block = simulink_block;
    }
    public simulink_Block getSimulink_block() {
        return simulink_block;
    }

    public void setSimulink_block(simulink_Block simulink_block) {
        this.simulink_block = simulink_block;
    }

}