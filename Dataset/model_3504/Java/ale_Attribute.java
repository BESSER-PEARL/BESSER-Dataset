





import java.util.List;
import java.util.ArrayList;

public class ale_Attribute  {

    private String bounds;
    private String modifier;
    private String name;





    private ale_BehavioredClass ale_behavioredclass;


    public ale_Attribute(
        String bounds,        String modifier,        String name    ) {
        this.bounds = bounds;
        this.modifier = modifier;
        this.name = name;
    }


    public String getBounds() {
        return bounds;
    }

    public void setBounds(String bounds) {
        this.bounds = bounds;
    }
    public String getModifier() {
        return modifier;
    }

    public void setModifier(String modifier) {
        this.modifier = modifier;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public ale_BehavioredClass getAle_behavioredclass() {
        return ale_behavioredclass;
    }

    public void setAle_behavioredclass(ale_BehavioredClass ale_behavioredclass) {
        this.ale_behavioredclass = ale_behavioredclass;
    }

}