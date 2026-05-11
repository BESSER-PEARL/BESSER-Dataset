





import java.util.List;
import java.util.ArrayList;

public class core_actionstep_ExecuteQuery extends actionstep_ActionStep, actionstep_Heavyweight {

    private String resultSetName;



    public core_actionstep_ExecuteQuery(
        String resultSetName    ) {
        super(
        );
        this.resultSetName = resultSetName;
    }


    public String getResultsetname() {
        return resultSetName;
    }

    public void setResultsetname(String resultSetName) {
        this.resultSetName = resultSetName;
    }


}