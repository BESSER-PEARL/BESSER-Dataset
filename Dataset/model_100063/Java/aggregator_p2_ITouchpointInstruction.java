





import java.util.List;
import java.util.ArrayList;

public class aggregator_p2_ITouchpointInstruction  {

    private String body;
    private String importAttribute;



    public aggregator_p2_ITouchpointInstruction(
        String body,        String importAttribute    ) {
        this.body = body;
        this.importAttribute = importAttribute;
    }


    public String getBody() {
        return body;
    }

    public void setBody(String body) {
        this.body = body;
    }
    public String getImportattribute() {
        return importAttribute;
    }

    public void setImportattribute(String importAttribute) {
        this.importAttribute = importAttribute;
    }


}