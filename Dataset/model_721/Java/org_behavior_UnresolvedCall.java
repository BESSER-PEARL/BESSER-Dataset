





import java.util.List;
import java.util.ArrayList;

public class org_behavior_UnresolvedCall extends structure_UnresolvedReference, behavior_CallExpression, structure_TypeContainer {

    private String isCalledWithParenthesis;
    private String isAtpre;



    public org_behavior_UnresolvedCall(
        String isCalledWithParenthesis,        String isAtpre    ) {
        super(
        );
        this.isCalledWithParenthesis = isCalledWithParenthesis;
        this.isAtpre = isAtpre;
    }


    public String getIscalledwithparenthesis() {
        return isCalledWithParenthesis;
    }

    public void setIscalledwithparenthesis(String isCalledWithParenthesis) {
        this.isCalledWithParenthesis = isCalledWithParenthesis;
    }
    public String getIsatpre() {
        return isAtpre;
    }

    public void setIsatpre(String isAtpre) {
        this.isAtpre = isAtpre;
    }


}