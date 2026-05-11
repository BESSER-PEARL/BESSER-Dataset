





import java.util.List;
import java.util.ArrayList;

public class bank_Token extends TransactionInitiator {

    private String value;





    private bank_Merchant bank_merchant;




    private bank_Device bank_device;


    public bank_Token(
        String value    ) {
        super(
        );
        this.value = value;
    }


    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }

    public bank_Merchant getBank_merchant() {
        return bank_merchant;
    }

    public void setBank_merchant(bank_Merchant bank_merchant) {
        this.bank_merchant = bank_merchant;
    }
    public bank_Device getBank_device() {
        return bank_device;
    }

    public void setBank_device(bank_Device bank_device) {
        this.bank_device = bank_device;
    }

}