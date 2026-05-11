





import java.util.List;
import java.util.ArrayList;

public class farrusco_StateOverride extends Behavior {

    private int succ_policy;
    private int runn_policy;
    private int fail_policy;



    public farrusco_StateOverride(
        int succ_policy,        int runn_policy,        int fail_policy    ) {
        super(
        );
        this.succ_policy = succ_policy;
        this.runn_policy = runn_policy;
        this.fail_policy = fail_policy;
    }


    public int getSucc_policy() {
        return succ_policy;
    }

    public void setSucc_policy(int succ_policy) {
        this.succ_policy = succ_policy;
    }
    public int getRunn_policy() {
        return runn_policy;
    }

    public void setRunn_policy(int runn_policy) {
        this.runn_policy = runn_policy;
    }
    public int getFail_policy() {
        return fail_policy;
    }

    public void setFail_policy(int fail_policy) {
        this.fail_policy = fail_policy;
    }


}