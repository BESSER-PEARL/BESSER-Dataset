





import java.util.List;
import java.util.ArrayList;

public class setup_P2Repository  {

    private String uRL;





    private setup_MaterializationTask setup_materializationtask;




    private setup_P2Task setup_p2task;


    public setup_P2Repository(
        String uRL    ) {
        this.uRL = uRL;
    }


    public String getUrl() {
        return uRL;
    }

    public void setUrl(String uRL) {
        this.uRL = uRL;
    }

    public setup_MaterializationTask getSetup_materializationtask() {
        return setup_materializationtask;
    }

    public void setSetup_materializationtask(setup_MaterializationTask setup_materializationtask) {
        this.setup_materializationtask = setup_materializationtask;
    }
    public setup_P2Task getSetup_p2task() {
        return setup_p2task;
    }

    public void setSetup_p2task(setup_P2Task setup_p2task) {
        this.setup_p2task = setup_p2task;
    }

}