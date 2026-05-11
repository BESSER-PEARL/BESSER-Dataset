





import java.util.List;
import java.util.ArrayList;

public class Message  {






    private model_Catch model_catch;




    private model_Variable model_variable;




    private model_OnEvent model_onevent;


    public Message(
    ) {
    }



    public model_Catch getModel_catch() {
        return model_catch;
    }

    public void setModel_catch(model_Catch model_catch) {
        this.model_catch = model_catch;
    }
    public model_Variable getModel_variable() {
        return model_variable;
    }

    public void setModel_variable(model_Variable model_variable) {
        this.model_variable = model_variable;
    }
    public model_OnEvent getModel_onevent() {
        return model_onevent;
    }

    public void setModel_onevent(model_OnEvent model_onevent) {
        this.model_onevent = model_onevent;
    }

}