





import java.util.List;
import java.util.ArrayList;

public class cSharpArchId_AbstractMethodDeclaration extends BodyDeclaration {






    private cSharpArchId_Type csharparchid_type;




    private List<cSharpArchId_TypeParameter> csharparchid_typeparameters;


    public cSharpArchId_AbstractMethodDeclaration(
    ) {
        super(
        );
        this.csharparchid_typeparameters = new ArrayList<>();
    }

    public cSharpArchId_AbstractMethodDeclaration(
        ArrayList<cSharpArchId_TypeParameter> csharparchid_typeparameters    ) {
        this.csharparchid_typeparameters = csharparchid_typeparameters;
    }


    public cSharpArchId_Type getCsharparchid_type() {
        return csharparchid_type;
    }

    public void setCsharparchid_type(cSharpArchId_Type csharparchid_type) {
        this.csharparchid_type = csharparchid_type;
    }
    public List<cSharpArchId_TypeParameter> getCsharparchid_typeparameters() {
        return csharparchid_typeparameters;
    }

    public void addCsharparchid_typeparameter(Csharparchid_typeparameter csharparchid_typeparameter) {
        this.csharparchid_typeparameters.add(csharparchid_typeparameter);
    }

}