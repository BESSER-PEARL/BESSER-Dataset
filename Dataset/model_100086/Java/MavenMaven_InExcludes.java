





import java.util.List;
import java.util.ArrayList;

public class MavenMaven_InExcludes extends Basic {

    private String unless;
    private String name;
    private String ifCondition;



    public MavenMaven_InExcludes(
        String unless,        String name,        String ifCondition    ) {
        super(
        );
        this.unless = unless;
        this.name = name;
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
    public String getIfcondition() {
        return ifCondition;
    }

    public void setIfcondition(String ifCondition) {
        this.ifCondition = ifCondition;
    }


}