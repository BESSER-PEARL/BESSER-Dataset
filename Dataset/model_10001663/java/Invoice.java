





import java.util.List;
import java.util.ArrayList;

public class Invoice  {

    private String num;
    private float amount;
    private String product;
    private int quantity;



    public Invoice(
        String num,        float amount,        String product,        int quantity    ) {
        this.num = num;
        this.amount = amount;
        this.product = product;
        this.quantity = quantity;
    }


    public String getNum() {
        return num;
    }

    public void setNum(String num) {
        this.num = num;
    }
    public float getAmount() {
        return amount;
    }

    public void setAmount(float amount) {
        this.amount = amount;
    }
    public String getProduct() {
        return product;
    }

    public void setProduct(String product) {
        this.product = product;
    }
    public int getQuantity() {
        return quantity;
    }

    public void setQuantity(int quantity) {
        this.quantity = quantity;
    }


}