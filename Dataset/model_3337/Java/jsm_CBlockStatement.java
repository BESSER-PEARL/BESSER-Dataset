





import java.util.List;
import java.util.ArrayList;

public class jsm_CBlockStatement extends AbstractCStatement {






    private List<jsm_AbstractCStatement> jsm_abstractcstatements;


    public jsm_CBlockStatement(
    ) {
        super(
        );
        this.jsm_abstractcstatements = new ArrayList<>();
    }

    public jsm_CBlockStatement(
        ArrayList<jsm_AbstractCStatement> jsm_abstractcstatements    ) {
        this.jsm_abstractcstatements = jsm_abstractcstatements;
    }


    public List<jsm_AbstractCStatement> getJsm_abstractcstatements() {
        return jsm_abstractcstatements;
    }

    public void addJsm_abstractcstatement(Jsm_abstractcstatement jsm_abstractcstatement) {
        this.jsm_abstractcstatements.add(jsm_abstractcstatement);
    }

}