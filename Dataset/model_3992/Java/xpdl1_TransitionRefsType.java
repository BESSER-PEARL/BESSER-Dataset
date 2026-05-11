





import java.util.List;
import java.util.ArrayList;

public class xpdl1_TransitionRefsType  {






    private List<xpdl1_TransitionRefType> xpdl1_transitionreftypes;




    private xpdl1_DocumentRoot xpdl1_documentroot;




    private xpdl1_SplitType xpdl1_splittype;


    public xpdl1_TransitionRefsType(
    ) {
        this.xpdl1_transitionreftypes = new ArrayList<>();
    }

    public xpdl1_TransitionRefsType(
        ArrayList<xpdl1_TransitionRefType> xpdl1_transitionreftypes    ) {
        this.xpdl1_transitionreftypes = xpdl1_transitionreftypes;
    }


    public List<xpdl1_TransitionRefType> getXpdl1_transitionreftypes() {
        return xpdl1_transitionreftypes;
    }

    public void addXpdl1_transitionreftype(Xpdl1_transitionreftype xpdl1_transitionreftype) {
        this.xpdl1_transitionreftypes.add(xpdl1_transitionreftype);
    }
    public xpdl1_DocumentRoot getXpdl1_documentroot() {
        return xpdl1_documentroot;
    }

    public void setXpdl1_documentroot(xpdl1_DocumentRoot xpdl1_documentroot) {
        this.xpdl1_documentroot = xpdl1_documentroot;
    }
    public xpdl1_SplitType getXpdl1_splittype() {
        return xpdl1_splittype;
    }

    public void setXpdl1_splittype(xpdl1_SplitType xpdl1_splittype) {
        this.xpdl1_splittype = xpdl1_splittype;
    }

}