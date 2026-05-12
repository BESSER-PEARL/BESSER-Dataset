





import java.util.List;
import java.util.ArrayList;

public class Offer  {

    private String endDate;
    private int id;
    private int discount;
    private String beginDate;





    private Product product;


    public Offer(
        String endDate,        int id,        int discount,        String beginDate    ) {
        this.endDate = endDate;
        this.id = id;
        this.discount = discount;
        this.beginDate = beginDate;
    }


    public String getEnddate() {
        return endDate;
    }

    public void setEnddate(String endDate) {
        this.endDate = endDate;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
    public int getDiscount() {
        return discount;
    }

    public void setDiscount(int discount) {
        this.discount = discount;
    }
    public String getBegindate() {
        return beginDate;
    }

    public void setBegindate(String beginDate) {
        this.beginDate = beginDate;
    }

    public Product getProduct() {
        return product;
    }

    public void setProduct(Product product) {
        this.product = product;
    }

}