





import java.util.List;
import java.util.ArrayList;

public class shr5_CyberwareModifikatioren extends ModifikatorAttribute {

    private int simRig;
    private boolean universalDataConnector;
    private int controlRig;
    private boolean riggerInterface;
    private boolean directNeuralInterface;



    public shr5_CyberwareModifikatioren(
        int simRig,        boolean universalDataConnector,        int controlRig,        boolean riggerInterface,        boolean directNeuralInterface    ) {
        super(
        );
        this.simRig = simRig;
        this.universalDataConnector = universalDataConnector;
        this.controlRig = controlRig;
        this.riggerInterface = riggerInterface;
        this.directNeuralInterface = directNeuralInterface;
    }


    public int getSimrig() {
        return simRig;
    }

    public void setSimrig(int simRig) {
        this.simRig = simRig;
    }
    public boolean getUniversaldataconnector() {
        return universalDataConnector;
    }

    public void setUniversaldataconnector(boolean universalDataConnector) {
        this.universalDataConnector = universalDataConnector;
    }
    public int getControlrig() {
        return controlRig;
    }

    public void setControlrig(int controlRig) {
        this.controlRig = controlRig;
    }
    public boolean getRiggerinterface() {
        return riggerInterface;
    }

    public void setRiggerinterface(boolean riggerInterface) {
        this.riggerInterface = riggerInterface;
    }
    public boolean getDirectneuralinterface() {
        return directNeuralInterface;
    }

    public void setDirectneuralinterface(boolean directNeuralInterface) {
        this.directNeuralInterface = directNeuralInterface;
    }


}