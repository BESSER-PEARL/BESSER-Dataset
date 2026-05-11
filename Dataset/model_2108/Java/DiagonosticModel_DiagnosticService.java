





import java.util.List;
import java.util.ArrayList;

public class DiagonosticModel_DiagnosticService extends Action {

    private String service;
    private String ecu;
    private String result;



    public DiagonosticModel_DiagnosticService(
        String service,        String ecu,        String result    ) {
        super(
        );
        this.service = service;
        this.ecu = ecu;
        this.result = result;
    }


    public String getService() {
        return service;
    }

    public void setService(String service) {
        this.service = service;
    }
    public String getEcu() {
        return ecu;
    }

    public void setEcu(String ecu) {
        this.ecu = ecu;
    }
    public String getResult() {
        return result;
    }

    public void setResult(String result) {
        this.result = result;
    }


}