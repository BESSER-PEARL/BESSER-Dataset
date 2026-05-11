





import java.util.List;
import java.util.ArrayList;

public class spinefm_SystemActionModel_SystemAction  {

    private String type;
    private String cpsHistory;





    private Step step;


    public spinefm_SystemActionModel_SystemAction(
        String type,        String cpsHistory    ) {
        this.type = type;
        this.cpsHistory = cpsHistory;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getCpshistory() {
        return cpsHistory;
    }

    public void setCpshistory(String cpsHistory) {
        this.cpsHistory = cpsHistory;
    }

    public Step getStep() {
        return step;
    }

    public void setStep(Step step) {
        this.step = step;
    }

}