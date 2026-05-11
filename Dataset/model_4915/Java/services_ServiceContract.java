





import java.util.List;
import java.util.ArrayList;

public class services_ServiceContract  {

    private String oLA;
    private String wLA;
    private String sLA;
    private String uC;



    public services_ServiceContract(
        String oLA,        String wLA,        String sLA,        String uC    ) {
        this.oLA = oLA;
        this.wLA = wLA;
        this.sLA = sLA;
        this.uC = uC;
    }


    public String getOla() {
        return oLA;
    }

    public void setOla(String oLA) {
        this.oLA = oLA;
    }
    public String getWla() {
        return wLA;
    }

    public void setWla(String wLA) {
        this.wLA = wLA;
    }
    public String getSla() {
        return sLA;
    }

    public void setSla(String sLA) {
        this.sLA = sLA;
    }
    public String getUc() {
        return uC;
    }

    public void setUc(String uC) {
        this.uC = uC;
    }


}