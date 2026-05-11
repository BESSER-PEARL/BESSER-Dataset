





import java.util.List;
import java.util.ArrayList;

public class MARTE_HwMemory_HwRAM extends HwMemory {

    private String organization;
    private String isStatic;
    private String isNonVolatile;
    private String writePolicy;
    private String repl_Policy;
    private String isSynchronous;



    public MARTE_HwMemory_HwRAM(
        String organization,        String isStatic,        String isNonVolatile,        String writePolicy,        String repl_Policy,        String isSynchronous    ) {
        super(
        );
        this.organization = organization;
        this.isStatic = isStatic;
        this.isNonVolatile = isNonVolatile;
        this.writePolicy = writePolicy;
        this.repl_Policy = repl_Policy;
        this.isSynchronous = isSynchronous;
    }


    public String getOrganization() {
        return organization;
    }

    public void setOrganization(String organization) {
        this.organization = organization;
    }
    public String getIsstatic() {
        return isStatic;
    }

    public void setIsstatic(String isStatic) {
        this.isStatic = isStatic;
    }
    public String getIsnonvolatile() {
        return isNonVolatile;
    }

    public void setIsnonvolatile(String isNonVolatile) {
        this.isNonVolatile = isNonVolatile;
    }
    public String getWritepolicy() {
        return writePolicy;
    }

    public void setWritepolicy(String writePolicy) {
        this.writePolicy = writePolicy;
    }
    public String getRepl_policy() {
        return repl_Policy;
    }

    public void setRepl_policy(String repl_Policy) {
        this.repl_Policy = repl_Policy;
    }
    public String getIssynchronous() {
        return isSynchronous;
    }

    public void setIssynchronous(String isSynchronous) {
        this.isSynchronous = isSynchronous;
    }


}