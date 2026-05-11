




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class ppo_PurchaseOrder  {

    private LocalDate orderDate;
    private String comment;





    private List<ppo_Item> ppo_items;


    public ppo_PurchaseOrder(
        LocalDate orderDate,        String comment    ) {
        this.orderDate = orderDate;
        this.comment = comment;
        this.ppo_items = new ArrayList<>();
    }

    public ppo_PurchaseOrder(
        LocalDate orderDate,        String comment        ArrayList<ppo_Item> ppo_items    ) {
        this.orderDate = orderDate;
        this.comment = comment;
        this.ppo_items = ppo_items;
    }

    public LocalDate getOrderdate() {
        return orderDate;
    }

    public void setOrderdate(LocalDate orderDate) {
        this.orderDate = orderDate;
    }
    public String getComment() {
        return comment;
    }

    public void setComment(String comment) {
        this.comment = comment;
    }

    public List<ppo_Item> getPpo_items() {
        return ppo_items;
    }

    public void addPpo_item(Ppo_item ppo_item) {
        this.ppo_items.add(ppo_item);
    }

}