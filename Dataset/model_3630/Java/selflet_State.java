





import java.util.List;
import java.util.ArrayList;

public class selflet_State  {

    private String name;





    private selflet_ComplexBehavior selflet_complexbehavior;




    private selflet_ElementaryBehavior selflet_elementarybehavior;




    private List<selflet_State> selflet_states;


    public selflet_State(
        String name    ) {
        this.name = name;
        this.selflet_states = new ArrayList<>();
    }

    public selflet_State(
        String name        ArrayList<selflet_State> selflet_states    ) {
        this.name = name;
        this.selflet_states = selflet_states;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public selflet_ComplexBehavior getSelflet_complexbehavior() {
        return selflet_complexbehavior;
    }

    public void setSelflet_complexbehavior(selflet_ComplexBehavior selflet_complexbehavior) {
        this.selflet_complexbehavior = selflet_complexbehavior;
    }
    public selflet_ElementaryBehavior getSelflet_elementarybehavior() {
        return selflet_elementarybehavior;
    }

    public void setSelflet_elementarybehavior(selflet_ElementaryBehavior selflet_elementarybehavior) {
        this.selflet_elementarybehavior = selflet_elementarybehavior;
    }
    public List<selflet_State> getSelflet_states() {
        return selflet_states;
    }

    public void addSelflet_state(Selflet_state selflet_state) {
        this.selflet_states.add(selflet_state);
    }

}