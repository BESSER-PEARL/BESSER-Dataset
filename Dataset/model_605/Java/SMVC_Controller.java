





import java.util.List;
import java.util.ArrayList;

public class SMVC_Controller  {

    private String url;
    private String operation;





    private SMVC_Controller smvc_controller;




    private SMVC_SMVCApplication smvc_smvcapplication;




    private SMVC_SMVCApplication smvc_smvcapplication;


    public SMVC_Controller(
        String url,        String operation    ) {
        this.url = url;
        this.operation = operation;
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

    public SMVC_Controller getSmvc_controller() {
        return smvc_controller;
    }

    public void setSmvc_controller(SMVC_Controller smvc_controller) {
        this.smvc_controller = smvc_controller;
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

}