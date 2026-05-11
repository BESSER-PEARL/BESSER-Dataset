





import java.util.List;
import java.util.ArrayList;

public class aggregator_p2_ITouchpointInstruction  {

    private String importAttribute;
    private String body;



    public aggregator_p2_ITouchpointInstruction(
        String importAttribute,        String body    ) {
        this.importAttribute = importAttribute;
        this.body = body;
    }


    public String getImportattribute() {
        return importAttribute;
    }

    public void setImportattribute(String importAttribute) {
        this.importAttribute = importAttribute;
    }
    public String getBody() {
        return body;
    }

    public void setBody(String body) {
        this.body = body;
    }


}