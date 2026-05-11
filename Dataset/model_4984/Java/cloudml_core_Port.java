





import java.util.List;
import java.util.ArrayList;

public class cloudml_core_Port extends CloudMLElementWithProperties {

    private boolean isLocal;
    private int portNumber;



    public cloudml_core_Port(
        boolean isLocal,        int portNumber    ) {
        super(
        );
        this.isLocal = isLocal;
        this.portNumber = portNumber;
    }


    public boolean getIslocal() {
        return isLocal;
    }

    public void setIslocal(boolean isLocal) {
        this.isLocal = isLocal;
    }
    public int getPortnumber() {
        return portNumber;
    }

    public void setPortnumber(int portNumber) {
        this.portNumber = portNumber;
    }


}