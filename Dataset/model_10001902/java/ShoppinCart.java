




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class ShoppinCart  {

    private LocalDate creationDate;





    private WebUser webuser;




    private ShoppinCart shoppincart;




    private Account account;




    private List<LineItem> lineitems;


    public ShoppinCart(
        LocalDate creationDate    ) {
        this.creationDate = creationDate;
        this.lineitems = new ArrayList<>();
    }

    public ShoppinCart(
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

    public WebUser getWebuser() {
        return webuser;
    }

    public void setWebuser(WebUser webuser) {
        this.webuser = webuser;
    }
    public ShoppinCart getShoppincart() {
        return shoppincart;
    }

    public void setShoppincart(ShoppinCart shoppincart) {
        this.shoppincart = shoppincart;
    }
    public Account getAccount() {
        return account;
    }

    public void setAccount(Account account) {
        this.account = account;
    }
    public List<LineItem> getLineitems() {
        return lineitems;
    }

    public void addLineitem(Lineitem lineitem) {
        this.lineitems.add(lineitem);
    }

}