





import java.util.List;
import java.util.ArrayList;

public class astm_IdentifierReference extends NameReference {






    private astm_TypeQualifiedIdentifierReference astm_typequalifiedidentifierreference;




    private astm_QualifiedIdentifierReference astm_qualifiedidentifierreference;


    public astm_IdentifierReference(
    ) {
        super(
        );
    }



    public astm_TypeQualifiedIdentifierReference getAstm_typequalifiedidentifierreference() {
        return astm_typequalifiedidentifierreference;
    }

    public void setAstm_typequalifiedidentifierreference(astm_TypeQualifiedIdentifierReference astm_typequalifiedidentifierreference) {
        this.astm_typequalifiedidentifierreference = astm_typequalifiedidentifierreference;
    }
    public astm_QualifiedIdentifierReference getAstm_qualifiedidentifierreference() {
        return astm_qualifiedidentifierreference;
    }

    public void setAstm_qualifiedidentifierreference(astm_QualifiedIdentifierReference astm_qualifiedidentifierreference) {
        this.astm_qualifiedidentifierreference = astm_qualifiedidentifierreference;
    }

}