





import java.util.List;
import java.util.ArrayList;

public class MARTE_HwMemory_HwCache extends HwMemory {

    private String writePolicy;
    private String structure;
    private String level;
    private String repl_Policy;
    private String type;



    public MARTE_HwMemory_HwCache(
        String writePolicy,        String structure,        String level,        String repl_Policy,        String type    ) {
        super(
        );
        this.writePolicy = writePolicy;
        this.structure = structure;
        this.level = level;
        this.repl_Policy = repl_Policy;
        this.type = type;
    }


    public String getWritepolicy() {
        return writePolicy;
    }

    public void setWritepolicy(String writePolicy) {
        this.writePolicy = writePolicy;
    }
    public String getStructure() {
        return structure;
    }

    public void setStructure(String structure) {
        this.structure = structure;
    }
    public String getLevel() {
        return level;
    }

    public void setLevel(String level) {
        this.level = level;
    }
    public String getRepl_policy() {
        return repl_Policy;
    }

    public void setRepl_policy(String repl_Policy) {
        this.repl_Policy = repl_Policy;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }


}