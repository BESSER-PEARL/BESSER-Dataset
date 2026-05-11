





import java.util.List;
import java.util.ArrayList;

public class esof_homework4_q2_PurchaseOrder  {

    private String comment;
    private String orderDate;



    public esof_homework4_q2_PurchaseOrder(
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


}