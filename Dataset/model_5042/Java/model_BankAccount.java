





import java.util.List;
import java.util.ArrayList;

public class model_BankAccount extends IEntity {

    private String iban;
    private String accountHolder;
    private String bic;
    private String bankName;
    private String bankCode;



    public model_BankAccount(
        String iban,        String accountHolder,        String bic,        String bankName,        String bankCode    ) {
        super(
        );
        this.iban = iban;
        this.accountHolder = accountHolder;
        this.bic = bic;
        this.bankName = bankName;
        this.bankCode = bankCode;
    }


    public String getIban() {
        return iban;
    }

    public void setIban(String iban) {
        this.iban = iban;
    }
    public String getAccountholder() {
        return accountHolder;
    }

    public void setAccountholder(String accountHolder) {
        this.accountHolder = accountHolder;
    }
    public String getBic() {
        return bic;
    }

    public void setBic(String bic) {
        this.bic = bic;
    }
    public String getBankname() {
        return bankName;
    }

    public void setBankname(String bankName) {
        this.bankName = bankName;
    }
    public String getBankcode() {
        return bankCode;
    }

    public void setBankcode(String bankCode) {
        this.bankCode = bankCode;
    }


}