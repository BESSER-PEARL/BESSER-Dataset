





import java.util.List;
import java.util.ArrayList;

public class sunBooks_PromotionType  {

    private String discount;
    private String none;





    private sunBooks_BookType sunbooks_booktype;


    public sunBooks_PromotionType(
        String discount,        String none    ) {
        this.discount = discount;
        this.none = none;
    }


    public String getDiscount() {
        return discount;
    }

    public void setDiscount(String discount) {
        this.discount = discount;
    }
    public String getNone() {
        return none;
    }

    public void setNone(String none) {
        this.none = none;
    }

    public sunBooks_BookType getSunbooks_booktype() {
        return sunbooks_booktype;
    }

    public void setSunbooks_booktype(sunBooks_BookType sunbooks_booktype) {
        this.sunbooks_booktype = sunbooks_booktype;
    }

}