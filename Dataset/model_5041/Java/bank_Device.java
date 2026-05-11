





import java.util.List;
import java.util.ArrayList;

public class bank_Device extends TransactionInitiator {






    private bank_CustomerAccount bank_customeraccount;


    public bank_Device(
    ) {
        super(
        );
    }



    public bank_CustomerAccount getBank_customeraccount() {
        return bank_customeraccount;
    }

    public void setBank_customeraccount(bank_CustomerAccount bank_customeraccount) {
        this.bank_customeraccount = bank_customeraccount;
    }

}