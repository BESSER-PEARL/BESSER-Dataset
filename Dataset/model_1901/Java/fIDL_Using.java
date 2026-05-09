





import java.util.List;
import java.util.ArrayList;

public class fIDL_Using  {

    private String importedNamespace;
    private String name;





    private fIDL_LibraryHeader fidl_libraryheader;


    public fIDL_Using(
        String importedNamespace,        String name    ) {
        this.importedNamespace = importedNamespace;
        this.name = name;
    }


    public String getImportednamespace() {
        return importedNamespace;
    }

    public void setImportednamespace(String importedNamespace) {
        this.importedNamespace = importedNamespace;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public fIDL_LibraryHeader getFidl_libraryheader() {
        return fidl_libraryheader;
    }

    public void setFidl_libraryheader(fIDL_LibraryHeader fidl_libraryheader) {
        this.fidl_libraryheader = fidl_libraryheader;
    }

}