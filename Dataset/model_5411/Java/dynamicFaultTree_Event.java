





import java.util.List;
import java.util.ArrayList;

public class dynamicFaultTree_Event extends Element {






    private List<dynamicFaultTree_Dependency> dynamicfaulttree_dependencys;




    private dynamicFaultTree_Dependency dynamicfaulttree_dependency;




    private dynamicFaultTree_Gate dynamicfaulttree_gate;




    private dynamicFaultTree_Gate dynamicfaulttree_gate;


    public dynamicFaultTree_Event(
    ) {
        super(
        );
        this.dynamicfaulttree_dependencys = new ArrayList<>();
    }

    public dynamicFaultTree_Event(
        ArrayList<dynamicFaultTree_Dependency> dynamicfaulttree_dependencys    ) {
        this.dynamicfaulttree_dependencys = dynamicfaulttree_dependencys;
    }


    public List<dynamicFaultTree_Dependency> getDynamicfaulttree_dependencys() {
        return dynamicfaulttree_dependencys;
    }

    public void addDynamicfaulttree_dependency(Dynamicfaulttree_dependency dynamicfaulttree_dependency) {
        this.dynamicfaulttree_dependencys.add(dynamicfaulttree_dependency);
    }
    public dynamicFaultTree_Dependency getDynamicfaulttree_dependency() {
        return dynamicfaulttree_dependency;
    }

    public void setDynamicfaulttree_dependency(dynamicFaultTree_Dependency dynamicfaulttree_dependency) {
        this.dynamicfaulttree_dependency = dynamicfaulttree_dependency;
    }
    public dynamicFaultTree_Gate getDynamicfaulttree_gate() {
        return dynamicfaulttree_gate;
    }

    public void setDynamicfaulttree_gate(dynamicFaultTree_Gate dynamicfaulttree_gate) {
        this.dynamicfaulttree_gate = dynamicfaulttree_gate;
    }
    public dynamicFaultTree_Gate getDynamicfaulttree_gate() {
        return dynamicfaulttree_gate;
    }

    public void setDynamicfaulttree_gate(dynamicFaultTree_Gate dynamicfaulttree_gate) {
        this.dynamicfaulttree_gate = dynamicfaulttree_gate;
    }

}