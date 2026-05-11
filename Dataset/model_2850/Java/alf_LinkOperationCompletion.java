





import java.util.List;
import java.util.ArrayList;

public class alf_LinkOperationCompletion  {

    private String linkOperation;





    private alf_NameToPrimaryExpression alf_nametoprimaryexpression;


    public alf_LinkOperationCompletion(
        String linkOperation    ) {
        this.linkOperation = linkOperation;
    }


    public String getLinkoperation() {
        return linkOperation;
    }

    public void setLinkoperation(String linkOperation) {
        this.linkOperation = linkOperation;
    }

    public alf_NameToPrimaryExpression getAlf_nametoprimaryexpression() {
        return alf_nametoprimaryexpression;
    }

    public void setAlf_nametoprimaryexpression(alf_NameToPrimaryExpression alf_nametoprimaryexpression) {
        this.alf_nametoprimaryexpression = alf_nametoprimaryexpression;
    }

}