





import java.util.List;
import java.util.ArrayList;

public class express_CaseAction  {

    private String value;





    private express_CaseStatement express_casestatement;


    public express_CaseAction(
        String value    ) {
        this.value = value;
    }


    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }

    public express_CaseStatement getExpress_casestatement() {
        return express_casestatement;
    }

    public void setExpress_casestatement(express_CaseStatement express_casestatement) {
        this.express_casestatement = express_casestatement;
    }

}