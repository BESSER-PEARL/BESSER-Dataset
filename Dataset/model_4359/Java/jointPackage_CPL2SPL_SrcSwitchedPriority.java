





import java.util.List;
import java.util.ArrayList;

public class jointPackage_CPL2SPL_SrcSwitchedPriority extends SrcNodeContainer {

    private String greater;
    private String less;
    private String equal;



    public jointPackage_CPL2SPL_SrcSwitchedPriority(
        String greater,        String less,        String equal    ) {
        super(
        );
        this.greater = greater;
        this.less = less;
        this.equal = equal;
    }


    public String getGreater() {
        return greater;
    }

    public void setGreater(String greater) {
        this.greater = greater;
    }
    public String getLess() {
        return less;
    }

    public void setLess(String less) {
        this.less = less;
    }
    public String getEqual() {
        return equal;
    }

    public void setEqual(String equal) {
        this.equal = equal;
    }


}