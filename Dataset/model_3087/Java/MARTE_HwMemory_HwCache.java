





import java.util.List;
import java.util.ArrayList;

public class MARTE_HwMemory_HwCache extends HwMemory {

    private String writePolicy;
    private String type;
    private String repl_Policy;





    private NFP_Natural nfp_natural;


    public MARTE_HwMemory_HwCache(
        String writePolicy,        String type,        String repl_Policy    ) {
        super(
        );
        this.writePolicy = writePolicy;
        this.type = type;
        this.repl_Policy = repl_Policy;
    }


    public String getWritepolicy() {
        return writePolicy;
    }

    public void setWritepolicy(String writePolicy) {
        this.writePolicy = writePolicy;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getRepl_policy() {
        return repl_Policy;
    }

    public void setRepl_policy(String repl_Policy) {
        this.repl_Policy = repl_Policy;
    }

    public NFP_Natural getNfp_natural() {
        return nfp_natural;
    }

    public void setNfp_natural(NFP_Natural nfp_natural) {
        this.nfp_natural = nfp_natural;
    }

}