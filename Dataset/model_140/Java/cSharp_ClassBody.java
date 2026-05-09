





import java.util.List;
import java.util.ArrayList;

public class cSharp_ClassBody  {






    private cSharp_ClassDeclaration csharp_classdeclaration;




    private List<cSharp_Attributes> csharp_attributess;


    public cSharp_ClassBody(
    ) {
        this.csharp_attributess = new ArrayList<>();
    }

    public cSharp_ClassBody(
        ArrayList<cSharp_Attributes> csharp_attributess    ) {
        this.csharp_attributess = csharp_attributess;
    }


    public cSharp_ClassDeclaration getCsharp_classdeclaration() {
        return csharp_classdeclaration;
    }

    public void setCsharp_classdeclaration(cSharp_ClassDeclaration csharp_classdeclaration) {
        this.csharp_classdeclaration = csharp_classdeclaration;
    }
    public List<cSharp_Attributes> getCsharp_attributess() {
        return csharp_attributess;
    }

    public void addCsharp_attributes(Csharp_attributes csharp_attributes) {
        this.csharp_attributess.add(csharp_attributes);
    }

}