





import java.util.List;
import java.util.ArrayList;

public class Ant_InExcludes extends Basic {

    private String unless;
    private String ifCondition;
    private String name;



    public Ant_InExcludes(
        String unless,        String ifCondition,        String name    ) {
        super(
        );
        this.unless = unless;
        this.ifCondition = ifCondition;
        this.name = name;
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


}