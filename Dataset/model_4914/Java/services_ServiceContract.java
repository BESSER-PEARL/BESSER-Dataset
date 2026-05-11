





import java.util.List;
import java.util.ArrayList;

public class services_ServiceContract  {

    private String wLA;
    private String uC;
    private String oLA;
    private String sLA;





    private services_Service services_service;


    public services_ServiceContract(
        String wLA,        String uC,        String oLA,        String sLA    ) {
        this.wLA = wLA;
        this.uC = uC;
        this.oLA = oLA;
        this.sLA = sLA;
    }


    public String getWla() {
        return wLA;
    }

    public void setWla(String wLA) {
        this.wLA = wLA;
    }
    public String getUc() {
        return uC;
    }

    public void setUc(String uC) {
        this.uC = uC;
    }
    public String getOla() {
        return oLA;
    }

    public void setOla(String oLA) {
        this.oLA = oLA;
    }
    public String getSla() {
        return sLA;
    }

    public void setSla(String sLA) {
        this.sLA = sLA;
    }

    public services_Service getServices_service() {
        return services_service;
    }

    public void setServices_service(services_Service services_service) {
        this.services_service = services_service;
    }

}