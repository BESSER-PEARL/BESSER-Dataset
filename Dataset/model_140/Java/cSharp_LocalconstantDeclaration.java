





import java.util.List;
import java.util.ArrayList;

public class cSharp_LocalconstantDeclaration  {






    private List<cSharp_ConstantDeclarator> csharp_constantdeclarators;




    private cSharp_Type csharp_type;




    private cSharp_ConstantDeclarator csharp_constantdeclarator;




    private cSharp_DeclarationStatment csharp_declarationstatment;


    public cSharp_LocalconstantDeclaration(
    ) {
        this.csharp_constantdeclarators = new ArrayList<>();
    }

    public cSharp_LocalconstantDeclaration(
        ArrayList<cSharp_ConstantDeclarator> csharp_constantdeclarators    ) {
        this.csharp_constantdeclarators = csharp_constantdeclarators;
    }


    public List<cSharp_ConstantDeclarator> getCsharp_constantdeclarators() {
        return csharp_constantdeclarators;
    }

    public void addCsharp_constantdeclarator(Csharp_constantdeclarator csharp_constantdeclarator) {
        this.csharp_constantdeclarators.add(csharp_constantdeclarator);
    }
    public cSharp_Type getCsharp_type() {
        return csharp_type;
    }

    public void setCsharp_type(cSharp_Type csharp_type) {
        this.csharp_type = csharp_type;
    }
    public cSharp_ConstantDeclarator getCsharp_constantdeclarator() {
        return csharp_constantdeclarator;
    }

    public void setCsharp_constantdeclarator(cSharp_ConstantDeclarator csharp_constantdeclarator) {
        this.csharp_constantdeclarator = csharp_constantdeclarator;
    }
    public cSharp_DeclarationStatment getCsharp_declarationstatment() {
        return csharp_declarationstatment;
    }

    public void setCsharp_declarationstatment(cSharp_DeclarationStatment csharp_declarationstatment) {
        this.csharp_declarationstatment = csharp_declarationstatment;
    }

}