





import java.util.List;
import java.util.ArrayList;

public class Model_EClassifier  {






    private Model_Variable model_variable;




    private Model_Port model_port;




    private Model_Event model_event;


    public Model_EClassifier(
    ) {
    }



    public Model_Variable getModel_variable() {
        return model_variable;
    }

    public void setModel_variable(Model_Variable model_variable) {
        this.model_variable = model_variable;
    }
    public Model_Port getModel_port() {
        return model_port;
    }

    public void setModel_port(Model_Port model_port) {
        this.model_port = model_port;
    }
    public Model_Event getModel_event() {
        return model_event;
    }

    public void setModel_event(Model_Event model_event) {
        this.model_event = model_event;
    }

}