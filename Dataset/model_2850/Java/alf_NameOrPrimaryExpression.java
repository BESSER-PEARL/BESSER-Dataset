





import java.util.List;
import java.util.ArrayList;

public class alf_NameOrPrimaryExpression  {






    private alf_PrimaryExpression alf_primaryexpression;




    private alf_NameToPrimaryExpression alf_nametoprimaryexpression;




    private alf_QualifiedNameWithoutBinding alf_qualifiednamewithoutbinding;


    public alf_NameOrPrimaryExpression(
    ) {
    }



    public alf_PrimaryExpression getAlf_primaryexpression() {
        return alf_primaryexpression;
    }

    public void setAlf_primaryexpression(alf_PrimaryExpression alf_primaryexpression) {
        this.alf_primaryexpression = alf_primaryexpression;
    }
    public alf_NameToPrimaryExpression getAlf_nametoprimaryexpression() {
        return alf_nametoprimaryexpression;
    }

    public void setAlf_nametoprimaryexpression(alf_NameToPrimaryExpression alf_nametoprimaryexpression) {
        this.alf_nametoprimaryexpression = alf_nametoprimaryexpression;
    }
    public alf_QualifiedNameWithoutBinding getAlf_qualifiednamewithoutbinding() {
        return alf_qualifiednamewithoutbinding;
    }

    public void setAlf_qualifiednamewithoutbinding(alf_QualifiedNameWithoutBinding alf_qualifiednamewithoutbinding) {
        this.alf_qualifiednamewithoutbinding = alf_qualifiednamewithoutbinding;
    }

}