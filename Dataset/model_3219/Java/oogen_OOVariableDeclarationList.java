





import java.util.List;
import java.util.ArrayList;

public class oogen_OOVariableDeclarationList extends OOStatement {






    private List<oogen_OOVariable> oogen_oovariables;


    public oogen_OOVariableDeclarationList(
    ) {
        super(
        );
        this.oogen_oovariables = new ArrayList<>();
    }

    public oogen_OOVariableDeclarationList(
        ArrayList<oogen_OOVariable> oogen_oovariables    ) {
        this.oogen_oovariables = oogen_oovariables;
    }


    public List<oogen_OOVariable> getOogen_oovariables() {
        return oogen_oovariables;
    }

    public void addOogen_oovariable(Oogen_oovariable oogen_oovariable) {
        this.oogen_oovariables.add(oogen_oovariable);
    }

}