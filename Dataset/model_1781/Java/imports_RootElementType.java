





import java.util.List;
import java.util.ArrayList;

public class imports_RootElementType  {

    private String importURI;





    private imports_DocumentRoot imports_documentroot;




    private imports_BookType imports_booktype;


    public imports_RootElementType(
        String importURI    ) {
        this.importURI = importURI;
    }


    public String getImporturi() {
        return importURI;
    }

    public void setImporturi(String importURI) {
        this.importURI = importURI;
    }

    public imports_DocumentRoot getImports_documentroot() {
        return imports_documentroot;
    }

    public void setImports_documentroot(imports_DocumentRoot imports_documentroot) {
        this.imports_documentroot = imports_documentroot;
    }
    public imports_BookType getImports_booktype() {
        return imports_booktype;
    }

    public void setImports_booktype(imports_BookType imports_booktype) {
        this.imports_booktype = imports_booktype;
    }

}