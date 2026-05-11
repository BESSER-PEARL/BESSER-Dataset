





import java.util.List;
import java.util.ArrayList;

public class wsmodel3_InputOrchestrator  {

    private String URI;





    private wsmodel3_OutputBridge wsmodel3_outputbridge;


    public wsmodel3_InputOrchestrator(
        String URI    ) {
        this.URI = URI;
    }


    public String getUri() {
        return URI;
    }

    public void setUri(String URI) {
        this.URI = URI;
    }

    public wsmodel3_OutputBridge getWsmodel3_outputbridge() {
        return wsmodel3_outputbridge;
    }

    public void setWsmodel3_outputbridge(wsmodel3_OutputBridge wsmodel3_outputbridge) {
        this.wsmodel3_outputbridge = wsmodel3_outputbridge;
    }

}