





import java.util.List;
import java.util.ArrayList;

public class cpntools_Port extends DiagramElement {

    private String portType;





    private cpntools_Place cpntools_place;


    public cpntools_Port(
        String portType    ) {
        super(
        );
        this.portType = portType;
    }


    public String getPorttype() {
        return portType;
    }

    public void setPorttype(String portType) {
        this.portType = portType;
    }

    public cpntools_Place getCpntools_place() {
        return cpntools_place;
    }

    public void setCpntools_place(cpntools_Place cpntools_place) {
        this.cpntools_place = cpntools_place;
    }

}