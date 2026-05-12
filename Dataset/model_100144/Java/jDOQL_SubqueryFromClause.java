





import java.util.List;
import java.util.ArrayList;

public class jDOQL_SubqueryFromClause  {

    private String candidateClassName;
    private boolean isExcludeSubclasses;



    public jDOQL_SubqueryFromClause(
        String candidateClassName,        boolean isExcludeSubclasses    ) {
        this.candidateClassName = candidateClassName;
        this.isExcludeSubclasses = isExcludeSubclasses;
    }


    public String getCandidateclassname() {
        return candidateClassName;
    }

    public void setCandidateclassname(String candidateClassName) {
        this.candidateClassName = candidateClassName;
    }
    public boolean getIsexcludesubclasses() {
        return isExcludeSubclasses;
    }

    public void setIsexcludesubclasses(boolean isExcludeSubclasses) {
        this.isExcludeSubclasses = isExcludeSubclasses;
    }


}