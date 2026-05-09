





import java.util.List;
import java.util.ArrayList;

public class cSharpArchId_AbstractTypeDeclaration extends Type {






    private List<cSharpArchId_Comment> csharparchid_comments;




    private cSharpArchId_Modifier csharparchid_modifier;




    private cSharpArchId_CompileUnit csharparchid_compileunit;




    private List<cSharpArchId_BodyDeclaration> csharparchid_bodydeclarations;




    private List<cSharpArchId_Comment> csharparchid_comments;


    public cSharpArchId_AbstractTypeDeclaration(
    ) {
        super(
        );
        this.csharparchid_comments = new ArrayList<>();
        this.csharparchid_bodydeclarations = new ArrayList<>();
        this.csharparchid_comments = new ArrayList<>();
    }

    public cSharpArchId_AbstractTypeDeclaration(
        ArrayList<cSharpArchId_Comment> csharparchid_comments,        ArrayList<cSharpArchId_BodyDeclaration> csharparchid_bodydeclarations,        ArrayList<cSharpArchId_Comment> csharparchid_comments    ) {
        this.csharparchid_comments = csharparchid_comments;
        this.csharparchid_bodydeclarations = csharparchid_bodydeclarations;
        this.csharparchid_comments = csharparchid_comments;
    }


    public List<cSharpArchId_Comment> getCsharparchid_comments() {
        return csharparchid_comments;
    }

    public void addCsharparchid_comment(Csharparchid_comment csharparchid_comment) {
        this.csharparchid_comments.add(csharparchid_comment);
    }
    public cSharpArchId_Modifier getCsharparchid_modifier() {
        return csharparchid_modifier;
    }

    public void setCsharparchid_modifier(cSharpArchId_Modifier csharparchid_modifier) {
        this.csharparchid_modifier = csharparchid_modifier;
    }
    public cSharpArchId_CompileUnit getCsharparchid_compileunit() {
        return csharparchid_compileunit;
    }

    public void setCsharparchid_compileunit(cSharpArchId_CompileUnit csharparchid_compileunit) {
        this.csharparchid_compileunit = csharparchid_compileunit;
    }
    public List<cSharpArchId_BodyDeclaration> getCsharparchid_bodydeclarations() {
        return csharparchid_bodydeclarations;
    }

    public void addCsharparchid_bodydeclaration(Csharparchid_bodydeclaration csharparchid_bodydeclaration) {
        this.csharparchid_bodydeclarations.add(csharparchid_bodydeclaration);
    }
    public List<cSharpArchId_Comment> getCsharparchid_comments() {
        return csharparchid_comments;
    }

    public void addCsharparchid_comment(Csharparchid_comment csharparchid_comment) {
        this.csharparchid_comments.add(csharparchid_comment);
    }

}