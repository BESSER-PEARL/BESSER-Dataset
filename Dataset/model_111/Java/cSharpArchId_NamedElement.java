





import java.util.List;
import java.util.ArrayList;

public class cSharpArchId_NamedElement extends ASTNode {

    private String name;





    private cSharpArchId_CompileUnit csharparchid_compileunit;


    public cSharpArchId_NamedElement(
        String name    ) {
        super(
        );
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public cSharpArchId_CompileUnit getCsharparchid_compileunit() {
        return csharparchid_compileunit;
    }

    public void setCsharparchid_compileunit(cSharpArchId_CompileUnit csharparchid_compileunit) {
        this.csharparchid_compileunit = csharparchid_compileunit;
    }

}