




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class creditcard  {

    private String issuer;
    private int number;
    private LocalDate expirationdate;



    public creditcard(
        String issuer,        int number,        LocalDate expirationdate    ) {
        this.issuer = issuer;
        this.number = number;
        this.expirationdate = expirationdate;
    }


    public String getIssuer() {
        return issuer;
    }

    public void setIssuer(String issuer) {
        this.issuer = issuer;
    }
    public int getNumber() {
        return number;
    }

    public void setNumber(int number) {
        this.number = number;
    }
    public LocalDate getExpirationdate() {
        return expirationdate;
    }

    public void setExpirationdate(LocalDate expirationdate) {
        this.expirationdate = expirationdate;
    }


}