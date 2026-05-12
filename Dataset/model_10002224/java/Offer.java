





import java.util.List;
import java.util.ArrayList;

public class Offer  {

    private int id;
    private String endDate;
    private String beginDate;
    private int discount;





    private Product product;


    public Offer(
        int id,        String endDate,        String beginDate,        int discount    ) {
        this.id = id;
        this.endDate = endDate;
        this.beginDate = beginDate;
        this.discount = discount;
    }


    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
    public String getEnddate() {
        return endDate;
    }

    public void setEnddate(String endDate) {
        this.endDate = endDate;
    }
    public String getBegindate() {
        return beginDate;
    }

    public void setBegindate(String beginDate) {
        this.beginDate = beginDate;
    }
    public int getDiscount() {
        return discount;
    }

    public void setDiscount(int discount) {
        this.discount = discount;
    }

    public Product getProduct() {
        return product;
    }

    public void setProduct(Product product) {
        this.product = product;
    }

}