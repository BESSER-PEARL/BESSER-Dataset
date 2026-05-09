





import java.util.List;
import java.util.ArrayList;

public class cSharp_MethodHeader  {

    private String modifier;





    private cSharp_TypeOrVoid csharp_typeorvoid;




    private cSharp_QualifiedIdentifier csharp_qualifiedidentifier;




    private cSharp_FormalParameterList csharp_formalparameterlist;




    private cSharp_MethodDeclaration csharp_methoddeclaration;


    public cSharp_MethodHeader(
        String modifier    ) {
        this.modifier = modifier;
    }


    public String getModifier() {
        return modifier;
    }

    public void setModifier(String modifier) {
        this.modifier = modifier;
    }

    public cSharp_TypeOrVoid getCsharp_typeorvoid() {
        return csharp_typeorvoid;
    }

    public void setCsharp_typeorvoid(cSharp_TypeOrVoid csharp_typeorvoid) {
        this.csharp_typeorvoid = csharp_typeorvoid;
    }
    public cSharp_QualifiedIdentifier getCsharp_qualifiedidentifier() {
        return csharp_qualifiedidentifier;
    }

    public void setCsharp_qualifiedidentifier(cSharp_QualifiedIdentifier csharp_qualifiedidentifier) {
        this.csharp_qualifiedidentifier = csharp_qualifiedidentifier;
    }
    public cSharp_FormalParameterList getCsharp_formalparameterlist() {
        return csharp_formalparameterlist;
    }

    public void setCsharp_formalparameterlist(cSharp_FormalParameterList csharp_formalparameterlist) {
        this.csharp_formalparameterlist = csharp_formalparameterlist;
    }
    public cSharp_MethodDeclaration getCsharp_methoddeclaration() {
        return csharp_methoddeclaration;
    }

    public void setCsharp_methoddeclaration(cSharp_MethodDeclaration csharp_methoddeclaration) {
        this.csharp_methoddeclaration = csharp_methoddeclaration;
    }

}