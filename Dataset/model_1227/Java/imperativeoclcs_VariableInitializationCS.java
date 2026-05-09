





import java.util.List;
import java.util.ArrayList;

public class imperativeoclcs_VariableInitializationCS extends StatementCS {

    private boolean withResult;
    private String simpleNameCS;



    public imperativeoclcs_VariableInitializationCS(
        boolean withResult,        String simpleNameCS    ) {
        super(
        );
        this.withResult = withResult;
        this.simpleNameCS = simpleNameCS;
    }


    public boolean getWithresult() {
        return withResult;
    }

    public void setWithresult(boolean withResult) {
        this.withResult = withResult;
    }
    public String getSimplenamecs() {
        return simpleNameCS;
    }

    public void setSimplenamecs(String simpleNameCS) {
        this.simpleNameCS = simpleNameCS;
    }


}