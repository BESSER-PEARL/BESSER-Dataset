





import java.util.List;
import java.util.ArrayList;

public class AbstractRequirement  {






    private Reqtify_Section reqtify_section;




    private Reqtify_MacroRequirement reqtify_macrorequirement;




    private Reqtify_CoverLink reqtify_coverlink;


    public AbstractRequirement(
    ) {
    }



    public Reqtify_Section getReqtify_section() {
        return reqtify_section;
    }

    public void setReqtify_section(Reqtify_Section reqtify_section) {
        this.reqtify_section = reqtify_section;
    }
    public Reqtify_MacroRequirement getReqtify_macrorequirement() {
        return reqtify_macrorequirement;
    }

    public void setReqtify_macrorequirement(Reqtify_MacroRequirement reqtify_macrorequirement) {
        this.reqtify_macrorequirement = reqtify_macrorequirement;
    }
    public Reqtify_CoverLink getReqtify_coverlink() {
        return reqtify_coverlink;
    }

    public void setReqtify_coverlink(Reqtify_CoverLink reqtify_coverlink) {
        this.reqtify_coverlink = reqtify_coverlink;
    }

}