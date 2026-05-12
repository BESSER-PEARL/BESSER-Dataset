




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class Package_ShoppingCart  {

    private LocalDate creationDate;





    private LineItem lineitem;




    private WebUser webuser;




    private Account account;


    public Package_ShoppingCart(
        LocalDate creationDate    ) {
        this.creationDate = creationDate;
    }


    public LocalDate getCreationdate() {
        return creationDate;
    }

    public void setCreationdate(LocalDate creationDate) {
        this.creationDate = creationDate;
    }

    public LineItem getLineitem() {
        return lineitem;
    }

    public void setLineitem(LineItem lineitem) {
        this.lineitem = lineitem;
    }
    public WebUser getWebuser() {
        return webuser;
    }

    public void setWebuser(WebUser webuser) {
        this.webuser = webuser;
    }
    public Account getAccount() {
        return account;
    }

    public void setAccount(Account account) {
        this.account = account;
    }

}