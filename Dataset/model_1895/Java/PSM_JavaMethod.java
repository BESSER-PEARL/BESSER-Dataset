





import java.util.List;
import java.util.ArrayList;

public class PSM_JavaMethod extends JavaElement {

    private String RootCallingMethod;





    private PSM_JavaMethod psm_javamethod;




    private PSM_JavaDataType psm_javadatatype;


    public PSM_JavaMethod(
        String RootCallingMethod    ) {
        super(
        );
        this.RootCallingMethod = RootCallingMethod;
    }


    public String getRootcallingmethod() {
        return RootCallingMethod;
    }

    public void setRootcallingmethod(String RootCallingMethod) {
        this.RootCallingMethod = RootCallingMethod;
    }

    public PSM_JavaMethod getPsm_javamethod() {
        return psm_javamethod;
    }

    public void setPsm_javamethod(PSM_JavaMethod psm_javamethod) {
        this.psm_javamethod = psm_javamethod;
    }
    public PSM_JavaDataType getPsm_javadatatype() {
        return psm_javadatatype;
    }

    public void setPsm_javadatatype(PSM_JavaDataType psm_javadatatype) {
        this.psm_javadatatype = psm_javadatatype;
    }

}