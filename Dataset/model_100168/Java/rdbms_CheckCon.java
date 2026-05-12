





import java.util.List;
import java.util.ArrayList;

public class rdbms_CheckCon extends Constraints {

    private String checkCondition;





    private rdbms_Table rdbms_table;


    public rdbms_CheckCon(
        String checkCondition    ) {
        super(
        );
        this.checkCondition = checkCondition;
    }


    public String getCheckcondition() {
        return checkCondition;
    }

    public void setCheckcondition(String checkCondition) {
        this.checkCondition = checkCondition;
    }

    public rdbms_Table getRdbms_table() {
        return rdbms_table;
    }

    public void setRdbms_table(rdbms_Table rdbms_table) {
        this.rdbms_table = rdbms_table;
    }

}