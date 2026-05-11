





import java.util.List;
import java.util.ArrayList;

public class cobol_containers_CompilationUnit extends NamedElement {






    private List<CompilationUnit> compilationunits;


    public cobol_containers_CompilationUnit(
    ) {
        super(
        );
        this.compilationunits = new ArrayList<>();
    }

    public cobol_containers_CompilationUnit(
        ArrayList<CompilationUnit> compilationunits    ) {
        this.compilationunits = compilationunits;
    }


    public List<CompilationUnit> getCompilationunits() {
        return compilationunits;
    }

    public void addCompilationunit(Compilationunit compilationunit) {
        this.compilationunits.add(compilationunit);
    }

}