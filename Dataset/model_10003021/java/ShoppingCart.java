




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class ShoppingCart  {

    private LocalDate creationDate;





    private Account account;




    private WebUser webuser;




    private List<LineItem> lineitems;


    public ShoppingCart(
        LocalDate creationDate    ) {
        this.creationDate = creationDate;
        this.lineitems = new ArrayList<>();
    }

    public ShoppingCart(
        LocalDate creationDate        ArrayList<LineItem> lineitems    ) {
        this.creationDate = creationDate;
        this.lineitems = lineitems;
    }

    public LocalDate getCreationdate() {
        return creationDate;
    }

    public void setCreationdate(LocalDate creationDate) {
        this.creationDate = creationDate;
    }

    public Account getAccount() {
        return account;
    }

    public void setAccount(Account account) {
        this.account = account;
    }
    public WebUser getWebuser() {
        return webuser;
    }

    public void setWebuser(WebUser webuser) {
        this.webuser = webuser;
    }
    public List<LineItem> getLineitems() {
        return lineitems;
    }

    public void addLineitem(Lineitem lineitem) {
        this.lineitems.add(lineitem);
    }

}