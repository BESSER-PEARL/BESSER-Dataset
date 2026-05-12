





import java.util.List;
import java.util.ArrayList;

public class Ant_Target  {

    private String description;
    private String unless;
    private String name;
    private String ifCondition;



    public Ant_Target(
        String description,        String unless,        String name,        String ifCondition    ) {
        this.description = description;
        this.unless = unless;
        this.name = name;
        this.ifCondition = ifCondition;
    }


    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public String getUnless() {
        return unless;
    }

    public void setUnless(String unless) {
        this.unless = unless;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getIfcondition() {
        return ifCondition;
    }

    public void setIfcondition(String ifCondition) {
        this.ifCondition = ifCondition;
    }


}