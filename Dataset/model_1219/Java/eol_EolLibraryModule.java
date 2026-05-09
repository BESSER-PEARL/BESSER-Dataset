





import java.util.List;
import java.util.ArrayList;

public class eol_EolLibraryModule extends EolElement {






    private List<eol_Import> eol_imports;




    private eol_Import eol_import;


    public eol_EolLibraryModule(
    ) {
        super(
        );
        this.eol_imports = new ArrayList<>();
    }

    public eol_EolLibraryModule(
        ArrayList<eol_Import> eol_imports    ) {
        this.eol_imports = eol_imports;
    }


    public List<eol_Import> getEol_imports() {
        return eol_imports;
    }

    public void addEol_import(Eol_import eol_import) {
        this.eol_imports.add(eol_import);
    }
    public eol_Import getEol_import() {
        return eol_import;
    }

    public void setEol_import(eol_Import eol_import) {
        this.eol_import = eol_import;
    }

}