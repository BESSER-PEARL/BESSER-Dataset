





import java.util.List;
import java.util.ArrayList;

public class SMVC_Controller  {

    private String url;
    private String operation;





    private SMVC_SMVCApplication smvc_smvcapplication;




    private SMVC_SMVCApplication smvc_smvcapplication;




    private List<SMVC_Controller> smvc_controllers;


    public SMVC_Controller(
        String url,        String operation    ) {
        this.url = url;
        this.operation = operation;
        this.smvc_controllers = new ArrayList<>();
    }

    public SMVC_Controller(
        String url,        String operation        ArrayList<SMVC_Controller> smvc_controllers    ) {
        this.url = url;
        this.operation = operation;
        this.smvc_controllers = smvc_controllers;
    }

    public String getUrl() {
        return url;
    }

    public void setUrl(String url) {
        this.url = url;
    }
    public String getOperation() {
        return operation;
    }

    public void setOperation(String operation) {
        this.operation = operation;
    }

    public SMVC_SMVCApplication getSmvc_smvcapplication() {
        return smvc_smvcapplication;
    }

    public void setSmvc_smvcapplication(SMVC_SMVCApplication smvc_smvcapplication) {
        this.smvc_smvcapplication = smvc_smvcapplication;
    }
    public SMVC_SMVCApplication getSmvc_smvcapplication() {
        return smvc_smvcapplication;
    }

    public void setSmvc_smvcapplication(SMVC_SMVCApplication smvc_smvcapplication) {
        this.smvc_smvcapplication = smvc_smvcapplication;
    }
    public List<SMVC_Controller> getSmvc_controllers() {
        return smvc_controllers;
    }

    public void addSmvc_controller(Smvc_controller smvc_controller) {
        this.smvc_controllers.add(smvc_controller);
    }

}