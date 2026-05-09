





import java.util.List;
import java.util.ArrayList;

public class cSharp_NonArrayType extends ArrayType {






    private cSharp_PrimaryExpression csharp_primaryexpression;




    private cSharp_QualifiedIdentifier csharp_qualifiedidentifier;


    public cSharp_NonArrayType(
    ) {
        super(
        );
    }



    public cSharp_PrimaryExpression getCsharp_primaryexpression() {
        return csharp_primaryexpression;
    }

    public void setCsharp_primaryexpression(cSharp_PrimaryExpression csharp_primaryexpression) {
        this.csharp_primaryexpression = csharp_primaryexpression;
    }
    public cSharp_QualifiedIdentifier getCsharp_qualifiedidentifier() {
        return csharp_qualifiedidentifier;
    }

    public void setCsharp_qualifiedidentifier(cSharp_QualifiedIdentifier csharp_qualifiedidentifier) {
        this.csharp_qualifiedidentifier = csharp_qualifiedidentifier;
    }

}