





import java.util.List;
import java.util.ArrayList;

public class domain_ExpressionPart  {

    private String uid;
    private String expressionType;
    private int order;





    private domain_EObject domain_eobject;




    private domain_ContextValue domain_contextvalue;


    public domain_ExpressionPart(
        String uid,        String expressionType,        int order    ) {
        this.uid = uid;
        this.expressionType = expressionType;
        this.order = order;
    }


    public String getUid() {
        return uid;
    }

    public void setUid(String uid) {
        this.uid = uid;
    }
    public String getExpressiontype() {
        return expressionType;
    }

    public void setExpressiontype(String expressionType) {
        this.expressionType = expressionType;
    }
    public int getOrder() {
        return order;
    }

    public void setOrder(int order) {
        this.order = order;
    }

    public domain_EObject getDomain_eobject() {
        return domain_eobject;
    }

    public void setDomain_eobject(domain_EObject domain_eobject) {
        this.domain_eobject = domain_eobject;
    }
    public domain_ContextValue getDomain_contextvalue() {
        return domain_contextvalue;
    }

    public void setDomain_contextvalue(domain_ContextValue domain_contextvalue) {
        this.domain_contextvalue = domain_contextvalue;
    }

}