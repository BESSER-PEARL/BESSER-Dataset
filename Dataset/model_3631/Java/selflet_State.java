





import java.util.List;
import java.util.ArrayList;

public class selflet_State  {

    private String name;





    private selflet_ElementaryBehavior selflet_elementarybehavior;




    private selflet_State selflet_state;




    private selflet_ComplexBehavior selflet_complexbehavior;


    public selflet_State(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public selflet_ElementaryBehavior getSelflet_elementarybehavior() {
        return selflet_elementarybehavior;
    }

    public void setSelflet_elementarybehavior(selflet_ElementaryBehavior selflet_elementarybehavior) {
        this.selflet_elementarybehavior = selflet_elementarybehavior;
    }
    public selflet_State getSelflet_state() {
        return selflet_state;
    }

    public void setSelflet_state(selflet_State selflet_state) {
        this.selflet_state = selflet_state;
    }
    public selflet_ComplexBehavior getSelflet_complexbehavior() {
        return selflet_complexbehavior;
    }

    public void setSelflet_complexbehavior(selflet_ComplexBehavior selflet_complexbehavior) {
        this.selflet_complexbehavior = selflet_complexbehavior;
    }

}