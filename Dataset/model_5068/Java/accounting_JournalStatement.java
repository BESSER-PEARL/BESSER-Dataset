





import java.util.List;
import java.util.ArrayList;

public class accounting_JournalStatement  {

    private String date;
    private String description;
    private String amount;





    private accounting_JournalGroup accounting_journalgroup;




    private accounting_Account accounting_account;




    private accounting_Vat accounting_vat;




    private accounting_Account accounting_account;


    public accounting_JournalStatement(
        String date,        String description,        String amount    ) {
        this.date = date;
        this.description = description;
        this.amount = amount;
    }


    public String getDate() {
        return date;
    }

    public void setDate(String date) {
        this.date = date;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public String getAmount() {
        return amount;
    }

    public void setAmount(String amount) {
        this.amount = amount;
    }

    public accounting_JournalGroup getAccounting_journalgroup() {
        return accounting_journalgroup;
    }

    public void setAccounting_journalgroup(accounting_JournalGroup accounting_journalgroup) {
        this.accounting_journalgroup = accounting_journalgroup;
    }
    public accounting_Account getAccounting_account() {
        return accounting_account;
    }

    public void setAccounting_account(accounting_Account accounting_account) {
        this.accounting_account = accounting_account;
    }
    public accounting_Vat getAccounting_vat() {
        return accounting_vat;
    }

    public void setAccounting_vat(accounting_Vat accounting_vat) {
        this.accounting_vat = accounting_vat;
    }
    public accounting_Account getAccounting_account() {
        return accounting_account;
    }

    public void setAccounting_account(accounting_Account accounting_account) {
        this.accounting_account = accounting_account;
    }

}