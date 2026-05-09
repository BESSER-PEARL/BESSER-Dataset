





import java.util.List;
import java.util.ArrayList;

public class DefinitionObject  {






    private gastm_Scope gastm_scope;




    private gastm_CompilationUnit gastm_compilationunit;




    private gastm_NameSpaceDefinition gastm_namespacedefinition;


    public DefinitionObject(
    ) {
    }



    public gastm_Scope getGastm_scope() {
        return gastm_scope;
    }

    public void setGastm_scope(gastm_Scope gastm_scope) {
        this.gastm_scope = gastm_scope;
    }
    public gastm_CompilationUnit getGastm_compilationunit() {
        return gastm_compilationunit;
    }

    public void setGastm_compilationunit(gastm_CompilationUnit gastm_compilationunit) {
        this.gastm_compilationunit = gastm_compilationunit;
    }
    public gastm_NameSpaceDefinition getGastm_namespacedefinition() {
        return gastm_namespacedefinition;
    }

    public void setGastm_namespacedefinition(gastm_NameSpaceDefinition gastm_namespacedefinition) {
        this.gastm_namespacedefinition = gastm_namespacedefinition;
    }

}