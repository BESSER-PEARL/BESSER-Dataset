





import java.util.List;
import java.util.ArrayList;

public class domain_OrderBy  {

    private String order;
    private String uid;





    private domain_Orders domain_orders;




    private domain_EObject domain_eobject;


    public domain_OrderBy(
        String order,        String uid    ) {
        this.order = order;
        this.uid = uid;
    }


    public String getOrder() {
        return order;
    }

    public void setOrder(String order) {
        this.order = order;
    }
    public String getUid() {
        return uid;
    }

    public void setUid(String uid) {
        this.uid = uid;
    }

    public domain_Orders getDomain_orders() {
        return domain_orders;
    }

    public void setDomain_orders(domain_Orders domain_orders) {
        this.domain_orders = domain_orders;
    }
    public domain_EObject getDomain_eobject() {
        return domain_eobject;
    }

    public void setDomain_eobject(domain_EObject domain_eobject) {
        this.domain_eobject = domain_eobject;
    }

}