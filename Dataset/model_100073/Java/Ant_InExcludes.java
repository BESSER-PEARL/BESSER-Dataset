





import java.util.List;
import java.util.ArrayList;

public class Ant_InExcludes extends Basic {

    private String name;
    private String ifCondition;
    private String unless;



    public Ant_InExcludes(
        String name,        String ifCondition,        String unless    ) {
        super(
        );
        this.name = name;
        this.ifCondition = ifCondition;
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
    public String getUnless() {
        return unless;
    }

    public void setUnless(String unless) {
        this.unless = unless;
    }


}