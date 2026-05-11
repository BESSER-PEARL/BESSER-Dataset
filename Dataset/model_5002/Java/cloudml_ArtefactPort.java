





import java.util.List;
import java.util.ArrayList;

public class cloudml_ArtefactPort extends WithProperties {

    private int portNumber;
    private boolean isRemote;



    public cloudml_ArtefactPort(
        int portNumber,        boolean isRemote    ) {
        super(
        );
        this.portNumber = portNumber;
        this.isRemote = isRemote;
    }


    public int getPortnumber() {
        return portNumber;
    }

    public void setPortnumber(int portNumber) {
        this.portNumber = portNumber;
    }
    public boolean getIsremote() {
        return isRemote;
    }

    public void setIsremote(boolean isRemote) {
        this.isRemote = isRemote;
    }


}