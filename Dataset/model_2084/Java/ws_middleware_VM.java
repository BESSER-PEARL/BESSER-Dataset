





import java.util.List;
import java.util.ArrayList;

public class ws_middleware_VM  {

    private String ID;
    private String protocol;



    public ws_middleware_VM(
        String ID,        String protocol    ) {
        this.ID = ID;
        this.protocol = protocol;
    }


    public String getId() {
        return ID;
    }

    public void setId(String ID) {
        this.ID = ID;
    }
    public String getProtocol() {
        return protocol;
    }

    public void setProtocol(String protocol) {
        this.protocol = protocol;
    }


}