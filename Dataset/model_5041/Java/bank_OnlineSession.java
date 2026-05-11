




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class bank_OnlineSession extends TransactionInitiator {

    private String internetAddress;
    private LocalDate start;
    private LocalDate end;





    private bank_Customer bank_customer;


    public bank_OnlineSession(
        String internetAddress,        LocalDate start,        LocalDate end    ) {
        super(
        );
        this.internetAddress = internetAddress;
        this.start = start;
        this.end = end;
    }


    public String getInternetaddress() {
        return internetAddress;
    }

    public void setInternetaddress(String internetAddress) {
        this.internetAddress = internetAddress;
    }
    public LocalDate getStart() {
        return start;
    }

    public void setStart(LocalDate start) {
        this.start = start;
    }
    public LocalDate getEnd() {
        return end;
    }

    public void setEnd(LocalDate end) {
        this.end = end;
    }

    public bank_Customer getBank_customer() {
        return bank_customer;
    }

    public void setBank_customer(bank_Customer bank_customer) {
        this.bank_customer = bank_customer;
    }

}