





import java.util.List;
import java.util.ArrayList;

public class model_xtype_XImportDeclaration  {

    private boolean static;
    private boolean wildcard;
    private boolean extension;
    private String importedNamespace;





    private JvmDeclaredType jvmdeclaredtype;


    public model_xtype_XImportDeclaration(
        boolean static,        boolean wildcard,        boolean extension,        String importedNamespace    ) {
        this.static = static;
        this.wildcard = wildcard;
        this.extension = extension;
        this.importedNamespace = importedNamespace;
    }


    public boolean getStatic() {
        return static;
    }

    public void setStatic(boolean static) {
        this.static = static;
    }
    public boolean getWildcard() {
        return wildcard;
    }

    public void setWildcard(boolean wildcard) {
        this.wildcard = wildcard;
    }
    public boolean getExtension() {
        return extension;
    }

    public void setExtension(boolean extension) {
        this.extension = extension;
    }
    public String getImportednamespace() {
        return importedNamespace;
    }

    public void setImportednamespace(String importedNamespace) {
        this.importedNamespace = importedNamespace;
    }

    public JvmDeclaredType getJvmdeclaredtype() {
        return jvmdeclaredtype;
    }

    public void setJvmdeclaredtype(JvmDeclaredType jvmdeclaredtype) {
        this.jvmdeclaredtype = jvmdeclaredtype;
    }

}