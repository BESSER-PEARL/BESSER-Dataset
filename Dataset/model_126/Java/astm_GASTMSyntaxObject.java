





import java.util.List;
import java.util.ArrayList;

public class astm_GASTMSyntaxObject extends GASTMObject {






    private List<astm_PreprocessorElement> astm_preprocessorelements;




    private astm_SourceLocation astm_sourcelocation;


    public astm_GASTMSyntaxObject(
    ) {
        super(
        );
        this.astm_preprocessorelements = new ArrayList<>();
    }

    public astm_GASTMSyntaxObject(
        ArrayList<astm_PreprocessorElement> astm_preprocessorelements    ) {
        this.astm_preprocessorelements = astm_preprocessorelements;
    }


    public List<astm_PreprocessorElement> getAstm_preprocessorelements() {
        return astm_preprocessorelements;
    }

    public void addAstm_preprocessorelement(Astm_preprocessorelement astm_preprocessorelement) {
        this.astm_preprocessorelements.add(astm_preprocessorelement);
    }
    public astm_SourceLocation getAstm_sourcelocation() {
        return astm_sourcelocation;
    }

    public void setAstm_sourcelocation(astm_SourceLocation astm_sourcelocation) {
        this.astm_sourcelocation = astm_sourcelocation;
    }

}