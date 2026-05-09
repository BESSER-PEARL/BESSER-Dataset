





import java.util.List;
import java.util.ArrayList;

public class PSM_JavaMethodParameter extends JavaDataField {

    private int ParameterOrder;





    private PSM_JavaMethod psm_javamethod;


    public PSM_JavaMethodParameter(
        int ParameterOrder    ) {
        super(
        );
        this.ParameterOrder = ParameterOrder;
    }


    public int getParameterorder() {
        return ParameterOrder;
    }

    public void setParameterorder(int ParameterOrder) {
        this.ParameterOrder = ParameterOrder;
    }

    public PSM_JavaMethod getPsm_javamethod() {
        return psm_javamethod;
    }

    public void setPsm_javamethod(PSM_JavaMethod psm_javamethod) {
        this.psm_javamethod = psm_javamethod;
    }

}