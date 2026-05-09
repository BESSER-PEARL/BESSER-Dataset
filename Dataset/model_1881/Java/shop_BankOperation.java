





import java.util.List;
import java.util.ArrayList;

public class shop_BankOperation extends Valuable {

    private String description;





    private shop_AccountBook shop_accountbook;


    public shop_BankOperation(
        String description    ) {
        super(
        );
        this.description = description;
    }


    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }

    public shop_AccountBook getShop_accountbook() {
        return shop_accountbook;
    }

    public void setShop_accountbook(shop_AccountBook shop_accountbook) {
        this.shop_accountbook = shop_accountbook;
    }

}