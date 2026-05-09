





import java.util.List;
import java.util.ArrayList;

public class imports_ImportingElement extends Commentable {






    private List<Import> imports;


    public imports_ImportingElement(
    ) {
        super(
        );
        this.imports = new ArrayList<>();
    }

    public imports_ImportingElement(
        ArrayList<Import> imports    ) {
        this.imports = imports;
    }


    public List<Import> getImports() {
        return imports;
    }

    public void addImport(Import import) {
        this.imports.add(import);
    }

}