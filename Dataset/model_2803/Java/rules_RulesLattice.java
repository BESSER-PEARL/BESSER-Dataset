





import java.util.List;
import java.util.ArrayList;

public class rules_RulesLattice  {

    private String source;
    private String target;



    public rules_RulesLattice(
        String source,        String target    ) {
        this.source = source;
        this.target = target;
    }


    public String getSource() {
        return source;
    }

    public void setSource(String source) {
        this.source = source;
    }
    public String getTarget() {
        return target;
    }

    public void setTarget(String target) {
        this.target = target;
    }


}