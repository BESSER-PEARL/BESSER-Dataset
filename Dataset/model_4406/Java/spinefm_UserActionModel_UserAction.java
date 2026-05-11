





import java.util.List;
import java.util.ArrayList;

public class spinefm_UserActionModel_UserAction  {

    private String type;





    private Step step;




    private ContextManager contextmanager;


    public spinefm_UserActionModel_UserAction(
        String type    ) {
        this.type = type;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public Step getStep() {
        return step;
    }

    public void setStep(Step step) {
        this.step = step;
    }
    public ContextManager getContextmanager() {
        return contextmanager;
    }

    public void setContextmanager(ContextManager contextmanager) {
        this.contextmanager = contextmanager;
    }

}