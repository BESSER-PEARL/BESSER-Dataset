





import java.util.List;
import java.util.ArrayList;

public class gmf_all_gmfgraph_Node extends AbstractNode {

    private String resizeConstraint;
    private String affixedParentSide;



    public gmf_all_gmfgraph_Node(
        String resizeConstraint,        String affixedParentSide    ) {
        super(
        );
        this.resizeConstraint = resizeConstraint;
        this.affixedParentSide = affixedParentSide;
    }


    public String getResizeconstraint() {
        return resizeConstraint;
    }

    public void setResizeconstraint(String resizeConstraint) {
        this.resizeConstraint = resizeConstraint;
    }
    public String getAffixedparentside() {
        return affixedParentSide;
    }

    public void setAffixedparentside(String affixedParentSide) {
        this.affixedParentSide = affixedParentSide;
    }


}