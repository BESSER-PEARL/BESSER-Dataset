





import java.util.List;
import java.util.ArrayList;

public class schemaprimerpo_PurchaseOrder  {

    private String comment;
    private String orderDate;





    private schemaprimerpo_DocumentRoot schemaprimerpo_documentroot;


    public schemaprimerpo_PurchaseOrder(
        String comment,        String orderDate    ) {
        this.comment = comment;
        this.orderDate = orderDate;
    }


    public String getComment() {
        return comment;
    }

    public void setComment(String comment) {
        this.comment = comment;
    }
    public String getOrderdate() {
        return orderDate;
    }

    public void setOrderdate(String orderDate) {
        this.orderDate = orderDate;
    }

    public schemaprimerpo_DocumentRoot getSchemaprimerpo_documentroot() {
        return schemaprimerpo_documentroot;
    }

    public void setSchemaprimerpo_documentroot(schemaprimerpo_DocumentRoot schemaprimerpo_documentroot) {
        this.schemaprimerpo_documentroot = schemaprimerpo_documentroot;
    }

}