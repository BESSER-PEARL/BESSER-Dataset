





import java.util.List;
import java.util.ArrayList;

public class ddsm_Port extends CloudElement {

    private String portNumber;
    private boolean isLocal;



    public ddsm_Port(
        String portNumber,        boolean isLocal    ) {
        super(
        );
        this.portNumber = portNumber;
        this.isLocal = isLocal;
    }


    public String getPortnumber() {
        return portNumber;
    }

    public void setPortnumber(String portNumber) {
        this.portNumber = portNumber;
    }
    public boolean getIslocal() {
        return isLocal;
    }

    public void setIslocal(boolean isLocal) {
        this.isLocal = isLocal;
    }


}