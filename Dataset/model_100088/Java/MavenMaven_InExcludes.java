





import java.util.List;
import java.util.ArrayList;

public class MavenMaven_InExcludes extends Basic {

    private String ifCondition;
    private String name;
    private String unless;





    private MavenMaven_PatternSet mavenmaven_patternset;


    public MavenMaven_InExcludes(
        String ifCondition,        String name,        String unless    ) {
        super(
        );
        this.ifCondition = ifCondition;
        this.name = name;
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
    public String getUnless() {
        return unless;
    }

    public void setUnless(String unless) {
        this.unless = unless;
    }

    public MavenMaven_PatternSet getMavenmaven_patternset() {
        return mavenmaven_patternset;
    }

    public void setMavenmaven_patternset(MavenMaven_PatternSet mavenmaven_patternset) {
        this.mavenmaven_patternset = mavenmaven_patternset;
    }

}