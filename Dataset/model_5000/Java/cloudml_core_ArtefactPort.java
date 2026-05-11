





import java.util.List;
import java.util.ArrayList;

public class cloudml_core_ArtefactPort extends WithProperties {

    private boolean isRemote;
    private int portNumber;



    public cloudml_core_ArtefactPort(
        boolean isRemote,        int portNumber    ) {
        super(
        );
        this.isRemote = isRemote;
        this.portNumber = portNumber;
    }


    public boolean getIsremote() {
        return isRemote;
    }

    public void setIsremote(boolean isRemote) {
        this.isRemote = isRemote;
    }
    public int getPortnumber() {
        return portNumber;
    }

    public void setPortnumber(int portNumber) {
        this.portNumber = portNumber;
    }


}