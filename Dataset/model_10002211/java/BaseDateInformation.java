





import java.util.List;
import java.util.ArrayList;

public class BaseDateInformation  {

    private String CreateDate;
    private String CreatedBy;
    private String LastModifedBy;
    private String LastModifedDate;





    private OnlineShop onlineshop;




    private Category category;




    private Product product;


    public BaseDateInformation(
        String CreateDate,        String CreatedBy,        String LastModifedBy,        String LastModifedDate    ) {
        this.CreateDate = CreateDate;
        this.CreatedBy = CreatedBy;
        this.LastModifedBy = LastModifedBy;
        this.LastModifedDate = LastModifedDate;
    }


    public String getCreatedate() {
        return CreateDate;
    }

    public void setCreatedate(String CreateDate) {
        this.CreateDate = CreateDate;
    }
    public String getCreatedby() {
        return CreatedBy;
    }

    public void setCreatedby(String CreatedBy) {
        this.CreatedBy = CreatedBy;
    }
    public String getLastmodifedby() {
        return LastModifedBy;
    }

    public void setLastmodifedby(String LastModifedBy) {
        this.LastModifedBy = LastModifedBy;
    }
    public String getLastmodifeddate() {
        return LastModifedDate;
    }

    public void setLastmodifeddate(String LastModifedDate) {
        this.LastModifedDate = LastModifedDate;
    }

    public OnlineShop getOnlineshop() {
        return onlineshop;
    }

    public void setOnlineshop(OnlineShop onlineshop) {
        this.onlineshop = onlineshop;
    }
    public Category getCategory() {
        return category;
    }

    public void setCategory(Category category) {
        this.category = category;
    }
    public Product getProduct() {
        return product;
    }

    public void setProduct(Product product) {
        this.product = product;
    }

}