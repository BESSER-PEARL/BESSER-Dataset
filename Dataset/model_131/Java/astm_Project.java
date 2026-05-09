





import java.util.List;
import java.util.ArrayList;

public class astm_Project extends GASTMSemanticObject {






    private astm_GlobalScope astm_globalscope;




    private List<astm_CompilationUnit> astm_compilationunits;


    public astm_Project(
    ) {
        super(
        );
        this.astm_compilationunits = new ArrayList<>();
    }

    public astm_Project(
        ArrayList<astm_CompilationUnit> astm_compilationunits    ) {
        this.astm_compilationunits = astm_compilationunits;
    }


    public astm_GlobalScope getAstm_globalscope() {
        return astm_globalscope;
    }

    public void setAstm_globalscope(astm_GlobalScope astm_globalscope) {
        this.astm_globalscope = astm_globalscope;
    }
    public List<astm_CompilationUnit> getAstm_compilationunits() {
        return astm_compilationunits;
    }

    public void addAstm_compilationunit(Astm_compilationunit astm_compilationunit) {
        this.astm_compilationunits.add(astm_compilationunit);
    }

}