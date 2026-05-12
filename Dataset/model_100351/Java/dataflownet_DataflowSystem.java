





import java.util.List;
import java.util.ArrayList;

public class dataflownet_DataflowSystem extends NamedElement {

    private String protocol;



    public dataflownet_DataflowSystem(
        String protocol    ) {
        super(
        );
        this.protocol = protocol;
    }


    public String getProtocol() {
        return protocol;
    }

    public void setProtocol(String protocol) {
        this.protocol = protocol;
    }


}