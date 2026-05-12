





import java.util.List;
import java.util.ArrayList;

public class Ant_Target  {

    private String unless;
    private String ifCondition;
    private String name;
    private String description;



    public Ant_Target(
        String unless,        String ifCondition,        String name,        String description    ) {
        this.unless = unless;
        this.ifCondition = ifCondition;
        this.name = name;
        this.description = description;
    }


    public String getUnless() {
        return unless;
    }

    public void setUnless(String unless) {
        this.unless = unless;
    }
    public String getIfcondition() {
        return ifCondition;
    }

    public void setIfcondition(String ifCondition) {
        this.ifCondition = ifCondition;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }


}