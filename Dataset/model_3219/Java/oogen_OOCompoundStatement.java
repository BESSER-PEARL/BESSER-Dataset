





import java.util.List;
import java.util.ArrayList;

public class oogen_OOCompoundStatement extends OOStatement {






    private List<oogen_OOStatement> oogen_oostatements;


    public oogen_OOCompoundStatement(
    ) {
        super(
        );
        this.oogen_oostatements = new ArrayList<>();
    }

    public oogen_OOCompoundStatement(
        ArrayList<oogen_OOStatement> oogen_oostatements    ) {
        this.oogen_oostatements = oogen_oostatements;
    }


    public List<oogen_OOStatement> getOogen_oostatements() {
        return oogen_oostatements;
    }

    public void addOogen_oostatement(Oogen_oostatement oogen_oostatement) {
        this.oogen_oostatements.add(oogen_oostatement);
    }

}