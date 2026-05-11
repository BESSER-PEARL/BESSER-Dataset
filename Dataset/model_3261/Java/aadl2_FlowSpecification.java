





import java.util.List;
import java.util.ArrayList;

public class aadl2_FlowSpecification extends ModalElement, Flow {

    private String kind;





    private aadl2_Context aadl2_context;




    private aadl2_FlowSpecification aadl2_flowspecification;




    private aadl2_Context aadl2_context;


    public aadl2_FlowSpecification(
        String kind    ) {
        super(
        );
        this.kind = kind;
    }


    public String getKind() {
        return kind;
    }

    public void setKind(String kind) {
        this.kind = kind;
    }

    public aadl2_Context getAadl2_context() {
        return aadl2_context;
    }

    public void setAadl2_context(aadl2_Context aadl2_context) {
        this.aadl2_context = aadl2_context;
    }
    public aadl2_FlowSpecification getAadl2_flowspecification() {
        return aadl2_flowspecification;
    }

    public void setAadl2_flowspecification(aadl2_FlowSpecification aadl2_flowspecification) {
        this.aadl2_flowspecification = aadl2_flowspecification;
    }
    public aadl2_Context getAadl2_context() {
        return aadl2_context;
    }

    public void setAadl2_context(aadl2_Context aadl2_context) {
        this.aadl2_context = aadl2_context;
    }

}