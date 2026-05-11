





import java.util.List;
import java.util.ArrayList;

public class web_service_Endpoint  {

    private String name;





    private web_service_Service web_service_service;


    public web_service_Endpoint(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public web_service_Service getWeb_service_service() {
        return web_service_service;
    }

    public void setWeb_service_service(web_service_Service web_service_service) {
        this.web_service_service = web_service_service;
    }

}