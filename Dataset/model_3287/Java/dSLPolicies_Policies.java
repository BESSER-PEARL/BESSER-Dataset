





import java.util.List;
import java.util.ArrayList;

public class dSLPolicies_Policies  {

    private boolean sync;
    private boolean nocheck;





    private dSLPolicies_GraphPolicies dslpolicies_graphpolicies;


    public dSLPolicies_Policies(
        boolean sync,        boolean nocheck    ) {
        this.sync = sync;
        this.nocheck = nocheck;
    }


    public boolean getSync() {
        return sync;
    }

    public void setSync(boolean sync) {
        this.sync = sync;
    }
    public boolean getNocheck() {
        return nocheck;
    }

    public void setNocheck(boolean nocheck) {
        this.nocheck = nocheck;
    }

    public dSLPolicies_GraphPolicies getDslpolicies_graphpolicies() {
        return dslpolicies_graphpolicies;
    }

    public void setDslpolicies_graphpolicies(dSLPolicies_GraphPolicies dslpolicies_graphpolicies) {
        this.dslpolicies_graphpolicies = dslpolicies_graphpolicies;
    }

}