





import java.util.List;
import java.util.ArrayList;

public class cloudml_core_Port extends CloudMLElementWithProperties {

    private int portNumber;
    private boolean isLocal;



    public cloudml_core_Port(
        int portNumber,        boolean isLocal    ) {
        super(
        );
        this.portNumber = portNumber;
        this.isLocal = isLocal;
    }


    public int getPortnumber() {
        return portNumber;
    }

    public void setPortnumber(int portNumber) {
        this.portNumber = portNumber;
    }
    public boolean getIslocal() {
        return isLocal;
    }

    public void setIslocal(boolean isLocal) {
        this.isLocal = isLocal;
    }


}