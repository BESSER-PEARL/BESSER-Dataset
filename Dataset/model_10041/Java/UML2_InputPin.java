





import java.util.List;
import java.util.ArrayList;

public class UML2_InputPin extends Pin {






    private UML2_LinkEndData uml2_linkenddata;




    private UML2_QualifierValue uml2_qualifiervalue;




    private UML2_Action uml2_action;


    public UML2_InputPin(
    ) {
        super(
        );
    }



    public UML2_LinkEndData getUml2_linkenddata() {
        return uml2_linkenddata;
    }

    public void setUml2_linkenddata(UML2_LinkEndData uml2_linkenddata) {
        this.uml2_linkenddata = uml2_linkenddata;
    }
    public UML2_QualifierValue getUml2_qualifiervalue() {
        return uml2_qualifiervalue;
    }

    public void setUml2_qualifiervalue(UML2_QualifierValue uml2_qualifiervalue) {
        this.uml2_qualifiervalue = uml2_qualifiervalue;
    }
    public UML2_Action getUml2_action() {
        return uml2_action;
    }

    public void setUml2_action(UML2_Action uml2_action) {
        this.uml2_action = uml2_action;
    }

}