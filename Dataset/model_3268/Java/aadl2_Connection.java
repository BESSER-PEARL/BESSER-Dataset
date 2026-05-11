





import java.util.List;
import java.util.ArrayList;

public class aadl2_Connection extends StructuralFeature, FlowElement, ModalPath {

    private String bidirectional;





    private aadl2_Connection aadl2_connection;




    private aadl2_ConnectedElement aadl2_connectedelement;




    private aadl2_ConnectedElement aadl2_connectedelement;


    public aadl2_Connection(
        String bidirectional    ) {
        super(
        );
        this.bidirectional = bidirectional;
    }


    public String getBidirectional() {
        return bidirectional;
    }

    public void setBidirectional(String bidirectional) {
        this.bidirectional = bidirectional;
    }

    public aadl2_Connection getAadl2_connection() {
        return aadl2_connection;
    }

    public void setAadl2_connection(aadl2_Connection aadl2_connection) {
        this.aadl2_connection = aadl2_connection;
    }
    public aadl2_ConnectedElement getAadl2_connectedelement() {
        return aadl2_connectedelement;
    }

    public void setAadl2_connectedelement(aadl2_ConnectedElement aadl2_connectedelement) {
        this.aadl2_connectedelement = aadl2_connectedelement;
    }
    public aadl2_ConnectedElement getAadl2_connectedelement() {
        return aadl2_connectedelement;
    }

    public void setAadl2_connectedelement(aadl2_ConnectedElement aadl2_connectedelement) {
        this.aadl2_connectedelement = aadl2_connectedelement;
    }

}