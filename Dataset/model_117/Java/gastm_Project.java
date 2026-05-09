





import java.util.List;
import java.util.ArrayList;

public class gastm_Project extends GASTMSemanticObject {






    private List<gastm_CompilationUnit> gastm_compilationunits;


    public gastm_Project(
    ) {
        super(
        );
        this.gastm_compilationunits = new ArrayList<>();
    }

    public gastm_Project(
        ArrayList<gastm_CompilationUnit> gastm_compilationunits    ) {
        this.gastm_compilationunits = gastm_compilationunits;
    }


    public List<gastm_CompilationUnit> getGastm_compilationunits() {
        return gastm_compilationunits;
    }

    public void addGastm_compilationunit(Gastm_compilationunit gastm_compilationunit) {
        this.gastm_compilationunits.add(gastm_compilationunit);
    }

}