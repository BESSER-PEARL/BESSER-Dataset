





import java.util.List;
import java.util.ArrayList;

public class cloudml_core_ArtefactPort extends WithProperties {

    private int portNumber;



    public cloudml_core_ArtefactPort(
        int portNumber    ) {
        super(
        );
        this.portNumber = portNumber;
    }


    public int getPortnumber() {
        return portNumber;
    }

    public void setPortnumber(int portNumber) {
        this.portNumber = portNumber;
    }


}