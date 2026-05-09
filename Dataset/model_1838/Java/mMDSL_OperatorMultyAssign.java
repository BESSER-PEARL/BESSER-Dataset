





import java.util.List;
import java.util.ArrayList;

public class mMDSL_OperatorMultyAssign  {

    private String divassign;
    private String multiassign;
    private String subassign;
    private String addassign;





    private mMDSL_OperatorAssign mmdsl_operatorassign;


    public mMDSL_OperatorMultyAssign(
        String divassign,        String multiassign,        String subassign,        String addassign    ) {
        this.divassign = divassign;
        this.multiassign = multiassign;
        this.subassign = subassign;
        this.addassign = addassign;
    }


    public String getDivassign() {
        return divassign;
    }

    public void setDivassign(String divassign) {
        this.divassign = divassign;
    }
    public String getMultiassign() {
        return multiassign;
    }

    public void setMultiassign(String multiassign) {
        this.multiassign = multiassign;
    }
    public String getSubassign() {
        return subassign;
    }

    public void setSubassign(String subassign) {
        this.subassign = subassign;
    }
    public String getAddassign() {
        return addassign;
    }

    public void setAddassign(String addassign) {
        this.addassign = addassign;
    }

    public mMDSL_OperatorAssign getMmdsl_operatorassign() {
        return mmdsl_operatorassign;
    }

    public void setMmdsl_operatorassign(mMDSL_OperatorAssign mmdsl_operatorassign) {
        this.mmdsl_operatorassign = mmdsl_operatorassign;
    }

}