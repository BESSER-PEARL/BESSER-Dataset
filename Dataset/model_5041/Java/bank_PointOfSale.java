





import java.util.List;
import java.util.ArrayList;

public class bank_PointOfSale  {

    private String id;





    private bank_Merchant bank_merchant;




    private bank_PostalAddress bank_postaladdress;


    public bank_PointOfSale(
        String id    ) {
        this.id = id;
    }


    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public bank_Merchant getBank_merchant() {
        return bank_merchant;
    }

    public void setBank_merchant(bank_Merchant bank_merchant) {
        this.bank_merchant = bank_merchant;
    }
    public bank_PostalAddress getBank_postaladdress() {
        return bank_postaladdress;
    }

    public void setBank_postaladdress(bank_PostalAddress bank_postaladdress) {
        this.bank_postaladdress = bank_postaladdress;
    }

}