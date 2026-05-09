





import java.util.List;
import java.util.ArrayList;

public class assessment_Http extends GraphNode {

    private String request;
    private String response;



    public assessment_Http(
        String request,        String response    ) {
        super(
        );
        this.request = request;
        this.response = response;
    }


    public String getRequest() {
        return request;
    }

    public void setRequest(String request) {
        this.request = request;
    }
    public String getResponse() {
        return response;
    }

    public void setResponse(String response) {
        this.response = response;
    }


}