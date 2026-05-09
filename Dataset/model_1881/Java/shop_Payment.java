





import java.util.List;
import java.util.ArrayList;

public class shop_Payment extends Valuable {

    private String type;





    private shop_AccountBook shop_accountbook;




    private shop_Sale shop_sale;




    private shop_Sale shop_sale;


    public shop_Payment(
        String type    ) {
        super(
        );
        this.type = type;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public shop_AccountBook getShop_accountbook() {
        return shop_accountbook;
    }

    public void setShop_accountbook(shop_AccountBook shop_accountbook) {
        this.shop_accountbook = shop_accountbook;
    }
    public shop_Sale getShop_sale() {
        return shop_sale;
    }

    public void setShop_sale(shop_Sale shop_sale) {
        this.shop_sale = shop_sale;
    }
    public shop_Sale getShop_sale() {
        return shop_sale;
    }

    public void setShop_sale(shop_Sale shop_sale) {
        this.shop_sale = shop_sale;
    }

}