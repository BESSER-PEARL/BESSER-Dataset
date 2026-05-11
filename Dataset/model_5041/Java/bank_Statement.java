




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class bank_Statement  {

    private String closingBalance;
    private String openingBalance;
    private LocalDate openingDate;
    private LocalDate closingDate;





    private bank_Account bank_account;


    public bank_Statement(
        String closingBalance,        String openingBalance,        LocalDate openingDate,        LocalDate closingDate    ) {
        this.closingBalance = closingBalance;
        this.openingBalance = openingBalance;
        this.openingDate = openingDate;
        this.closingDate = closingDate;
    }


    public String getClosingbalance() {
        return closingBalance;
    }

    public void setClosingbalance(String closingBalance) {
        this.closingBalance = closingBalance;
    }
    public String getOpeningbalance() {
        return openingBalance;
    }

    public void setOpeningbalance(String openingBalance) {
        this.openingBalance = openingBalance;
    }
    public LocalDate getOpeningdate() {
        return openingDate;
    }

    public void setOpeningdate(LocalDate openingDate) {
        this.openingDate = openingDate;
    }
    public LocalDate getClosingdate() {
        return closingDate;
    }

    public void setClosingdate(LocalDate closingDate) {
        this.closingDate = closingDate;
    }

    public bank_Account getBank_account() {
        return bank_account;
    }

    public void setBank_account(bank_Account bank_account) {
        this.bank_account = bank_account;
    }

}