





import java.util.List;
import java.util.ArrayList;

public class gmfgraph_Node extends AbstractNode {

    private String affixedParentSide;
    private String resizeConstraint;



    public gmfgraph_Node(
        String affixedParentSide,        String resizeConstraint    ) {
        super(
        );
        this.affixedParentSide = affixedParentSide;
        this.resizeConstraint = resizeConstraint;
    }


    public String getAffixedparentside() {
        return affixedParentSide;
    }

    public void setAffixedparentside(String affixedParentSide) {
        this.affixedParentSide = affixedParentSide;
    }
    public String getResizeconstraint() {
        return resizeConstraint;
    }

    public void setResizeconstraint(String resizeConstraint) {
        this.resizeConstraint = resizeConstraint;
    }


}