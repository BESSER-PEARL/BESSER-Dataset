





import java.util.List;
import java.util.ArrayList;

public class selflet_Actions  {






    private List<selflet_Action> selflet_actions;




    private selflet_SelfletResources selflet_selfletresources;


    public selflet_Actions(
    ) {
        this.selflet_actions = new ArrayList<>();
    }

    public selflet_Actions(
        ArrayList<selflet_Action> selflet_actions    ) {
        this.selflet_actions = selflet_actions;
    }


    public List<selflet_Action> getSelflet_actions() {
        return selflet_actions;
    }

    public void addSelflet_action(Selflet_action selflet_action) {
        this.selflet_actions.add(selflet_action);
    }
    public selflet_SelfletResources getSelflet_selfletresources() {
        return selflet_selfletresources;
    }

    public void setSelflet_selfletresources(selflet_SelfletResources selflet_selfletresources) {
        this.selflet_selfletresources = selflet_selfletresources;
    }

}