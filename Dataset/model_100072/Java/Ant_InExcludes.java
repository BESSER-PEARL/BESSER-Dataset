





import java.util.List;
import java.util.ArrayList;

public class Ant_InExcludes extends Basic {

    private String ifCondition;
    private String unless;
    private String name;



    public Ant_InExcludes(
        String ifCondition,        String unless,        String name    ) {
        super(
        );
        this.ifCondition = ifCondition;
        this.unless = unless;
        this.name = name;
    }


    public String getIfcondition() {
        return ifCondition;
    }

    public void setIfcondition(String ifCondition) {
        this.ifCondition = ifCondition;
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


}