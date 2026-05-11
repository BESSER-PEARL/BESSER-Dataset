





import java.util.List;
import java.util.ArrayList;

public class aadl2_Connection extends FlowElement, StructuralFeature, ModalPath {

    private String bidirectional;
    private String kind;





    private aadl2_Connection aadl2_connection;




    private aadl2_ConnectionEnd aadl2_connectionend;




    private aadl2_ConnectionEnd aadl2_connectionend;




    private aadl2_Context aadl2_context;




    private aadl2_Context aadl2_context;


    public aadl2_Connection(
        String bidirectional,        String kind    ) {
        super(
        );
        this.bidirectional = bidirectional;
        this.kind = kind;
    }


    public String getBidirectional() {
        return bidirectional;
    }

    public void setBidirectional(String bidirectional) {
        this.bidirectional = bidirectional;
    }
    public String getKind() {
        return kind;
    }

    public void setKind(String kind) {
        this.kind = kind;
    }

    public aadl2_Connection getAadl2_connection() {
        return aadl2_connection;
    }

    public void setAadl2_connection(aadl2_Connection aadl2_connection) {
        this.aadl2_connection = aadl2_connection;
    }
    public aadl2_ConnectionEnd getAadl2_connectionend() {
        return aadl2_connectionend;
    }

    public void setAadl2_connectionend(aadl2_ConnectionEnd aadl2_connectionend) {
        this.aadl2_connectionend = aadl2_connectionend;
    }
    public aadl2_ConnectionEnd getAadl2_connectionend() {
        return aadl2_connectionend;
    }

    public void setAadl2_connectionend(aadl2_ConnectionEnd aadl2_connectionend) {
        this.aadl2_connectionend = aadl2_connectionend;
    }
    public aadl2_Context getAadl2_context() {
        return aadl2_context;
    }

    public void setAadl2_context(aadl2_Context aadl2_context) {
        this.aadl2_context = aadl2_context;
    }
    public aadl2_Context getAadl2_context() {
        return aadl2_context;
    }

    public void setAadl2_context(aadl2_Context aadl2_context) {
        this.aadl2_context = aadl2_context;
    }

}