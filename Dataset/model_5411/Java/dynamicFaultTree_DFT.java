





import java.util.List;
import java.util.ArrayList;

public class dynamicFaultTree_DFT  {

    private String name;





    private List<dynamicFaultTree_Dependency> dynamicfaulttree_dependencys;




    private dynamicFaultTree_TopLevelEvent dynamicfaulttree_toplevelevent;


    public dynamicFaultTree_DFT(
        String name    ) {
        this.name = name;
        this.dynamicfaulttree_dependencys = new ArrayList<>();
    }

    public dynamicFaultTree_DFT(
        String name        ArrayList<dynamicFaultTree_Dependency> dynamicfaulttree_dependencys    ) {
        this.name = name;
        this.dynamicfaulttree_dependencys = dynamicfaulttree_dependencys;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<dynamicFaultTree_Dependency> getDynamicfaulttree_dependencys() {
        return dynamicfaulttree_dependencys;
    }

    public void addDynamicfaulttree_dependency(Dynamicfaulttree_dependency dynamicfaulttree_dependency) {
        this.dynamicfaulttree_dependencys.add(dynamicfaulttree_dependency);
    }
    public dynamicFaultTree_TopLevelEvent getDynamicfaulttree_toplevelevent() {
        return dynamicfaulttree_toplevelevent;
    }

    public void setDynamicfaulttree_toplevelevent(dynamicFaultTree_TopLevelEvent dynamicfaulttree_toplevelevent) {
        this.dynamicfaulttree_toplevelevent = dynamicfaulttree_toplevelevent;
    }

}