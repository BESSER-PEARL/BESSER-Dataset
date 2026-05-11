





import java.util.List;
import java.util.ArrayList;

public class aadl2_ConnectedElement extends Element {






    private aadl2_ConnectedElement aadl2_connectedelement;




    private aadl2_Context aadl2_context;




    private aadl2_ConnectionEnd aadl2_connectionend;


    public aadl2_ConnectedElement(
    ) {
        super(
        );
    }



    public aadl2_ConnectedElement getAadl2_connectedelement() {
        return aadl2_connectedelement;
    }

    public void setAadl2_connectedelement(aadl2_ConnectedElement aadl2_connectedelement) {
        this.aadl2_connectedelement = aadl2_connectedelement;
    }
    public aadl2_Context getAadl2_context() {
        return aadl2_context;
    }

    public void setAadl2_context(aadl2_Context aadl2_context) {
        this.aadl2_context = aadl2_context;
    }
    public aadl2_ConnectionEnd getAadl2_connectionend() {
        return aadl2_connectionend;
    }

    public void setAadl2_connectionend(aadl2_ConnectionEnd aadl2_connectionend) {
        this.aadl2_connectionend = aadl2_connectionend;
    }

}