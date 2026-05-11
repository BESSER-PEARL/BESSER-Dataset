





import java.util.List;
import java.util.ArrayList;

public class jointPackage_CPL2SPL_TrgLocalFunctionDeclaration extends TrgFunctionDeclaration {






    private List<TrgStatement> trgstatements;


    public jointPackage_CPL2SPL_TrgLocalFunctionDeclaration(
    ) {
        super(
        );
        this.trgstatements = new ArrayList<>();
    }

    public jointPackage_CPL2SPL_TrgLocalFunctionDeclaration(
        ArrayList<TrgStatement> trgstatements    ) {
        this.trgstatements = trgstatements;
    }


    public List<TrgStatement> getTrgstatements() {
        return trgstatements;
    }

    public void addTrgstatement(Trgstatement trgstatement) {
        this.trgstatements.add(trgstatement);
    }

}