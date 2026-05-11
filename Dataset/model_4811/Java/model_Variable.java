





import java.util.List;
import java.util.ArrayList;

public class model_Variable extends BPELExtensibleElement {

    private String name;





    private model_OnMessage model_onmessage;




    private model_FromPart model_frompart;




    private model_Variables model_variables;




    private model_OnEvent model_onevent;


    public model_Variable(
        String name    ) {
        super(
        );
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public model_OnMessage getModel_onmessage() {
        return model_onmessage;
    }

    public void setModel_onmessage(model_OnMessage model_onmessage) {
        this.model_onmessage = model_onmessage;
    }
    public model_FromPart getModel_frompart() {
        return model_frompart;
    }

    public void setModel_frompart(model_FromPart model_frompart) {
        this.model_frompart = model_frompart;
    }
    public model_Variables getModel_variables() {
        return model_variables;
    }

    public void setModel_variables(model_Variables model_variables) {
        this.model_variables = model_variables;
    }
    public model_OnEvent getModel_onevent() {
        return model_onevent;
    }

    public void setModel_onevent(model_OnEvent model_onevent) {
        this.model_onevent = model_onevent;
    }

}