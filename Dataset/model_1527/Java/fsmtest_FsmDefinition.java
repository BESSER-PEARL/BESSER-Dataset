





import java.util.List;
import java.util.ArrayList;

public class fsmtest_FsmDefinition  {

    private String name;





    private fsmtest_Model fsmtest_model;


    public fsmtest_FsmDefinition(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public fsmtest_Model getFsmtest_model() {
        return fsmtest_model;
    }

    public void setFsmtest_model(fsmtest_Model fsmtest_model) {
        this.fsmtest_model = fsmtest_model;
    }

}