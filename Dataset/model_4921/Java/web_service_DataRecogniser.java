





import java.util.List;
import java.util.ArrayList;

public class web_service_DataRecogniser  {

    private String name;





    private web_service_Endpoint web_service_endpoint;


    public web_service_DataRecogniser(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public web_service_Endpoint getWeb_service_endpoint() {
        return web_service_endpoint;
    }

    public void setWeb_service_endpoint(web_service_Endpoint web_service_endpoint) {
        this.web_service_endpoint = web_service_endpoint;
    }

}