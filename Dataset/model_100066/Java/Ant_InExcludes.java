





import java.util.List;
import java.util.ArrayList;

public class Ant_InExcludes extends Basic {

    private String name;
    private String unless;
    private String ifCondition;



    public Ant_InExcludes(
        String name,        String unless,        String ifCondition    ) {
        super(
        );
        this.name = name;
        this.unless = unless;
        this.ifCondition = ifCondition;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
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


}