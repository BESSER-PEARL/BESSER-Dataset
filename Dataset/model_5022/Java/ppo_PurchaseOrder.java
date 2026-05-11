





import java.util.List;
import java.util.ArrayList;

public class ppo_PurchaseOrder  {

    private String comment;
    private String orderDate;





    private ppo_USAddress ppo_usaddress;




    private ppo_USAddress ppo_usaddress;


    public ppo_PurchaseOrder(
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

    public ppo_USAddress getPpo_usaddress() {
        return ppo_usaddress;
    }

    public void setPpo_usaddress(ppo_USAddress ppo_usaddress) {
        this.ppo_usaddress = ppo_usaddress;
    }
    public ppo_USAddress getPpo_usaddress() {
        return ppo_usaddress;
    }

    public void setPpo_usaddress(ppo_USAddress ppo_usaddress) {
        this.ppo_usaddress = ppo_usaddress;
    }

}