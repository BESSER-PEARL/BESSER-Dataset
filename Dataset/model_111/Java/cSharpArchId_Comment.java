





import java.util.List;
import java.util.ArrayList;

public class cSharpArchId_Comment extends ASTNode {

    private String content;





    private cSharpArchId_CompileUnit csharparchid_compileunit;


    public cSharpArchId_Comment(
        String content    ) {
        super(
        );
        this.content = content;
    }


    public String getContent() {
        return content;
    }

    public void setContent(String content) {
        this.content = content;
    }

    public cSharpArchId_CompileUnit getCsharparchid_compileunit() {
        return csharparchid_compileunit;
    }

    public void setCsharparchid_compileunit(cSharpArchId_CompileUnit csharparchid_compileunit) {
        this.csharparchid_compileunit = csharparchid_compileunit;
    }

}