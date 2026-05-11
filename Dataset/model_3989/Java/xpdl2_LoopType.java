





import java.util.List;
import java.util.ArrayList;

public class xpdl2_LoopType  {

    private String loopType;





    private xpdl2_LoopMultiInstanceType xpdl2_loopmultiinstancetype;




    private xpdl2_LoopStandardType xpdl2_loopstandardtype;


    public xpdl2_LoopType(
        String loopType    ) {
        this.loopType = loopType;
    }


    public String getLooptype() {
        return loopType;
    }

    public void setLooptype(String loopType) {
        this.loopType = loopType;
    }

    public xpdl2_LoopMultiInstanceType getXpdl2_loopmultiinstancetype() {
        return xpdl2_loopmultiinstancetype;
    }

    public void setXpdl2_loopmultiinstancetype(xpdl2_LoopMultiInstanceType xpdl2_loopmultiinstancetype) {
        this.xpdl2_loopmultiinstancetype = xpdl2_loopmultiinstancetype;
    }
    public xpdl2_LoopStandardType getXpdl2_loopstandardtype() {
        return xpdl2_loopstandardtype;
    }

    public void setXpdl2_loopstandardtype(xpdl2_LoopStandardType xpdl2_loopstandardtype) {
        this.xpdl2_loopstandardtype = xpdl2_loopstandardtype;
    }

}