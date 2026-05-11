





import java.util.List;
import java.util.ArrayList;

public class model_CBlockStatement extends AbstractCStatement {






    private List<model_AbstractCStatement> model_abstractcstatements;


    public model_CBlockStatement(
    ) {
        super(
        );
        this.model_abstractcstatements = new ArrayList<>();
    }

    public model_CBlockStatement(
        ArrayList<model_AbstractCStatement> model_abstractcstatements    ) {
        this.model_abstractcstatements = model_abstractcstatements;
    }


    public List<model_AbstractCStatement> getModel_abstractcstatements() {
        return model_abstractcstatements;
    }

    public void addModel_abstractcstatement(Model_abstractcstatement model_abstractcstatement) {
        this.model_abstractcstatements.add(model_abstractcstatement);
    }

}