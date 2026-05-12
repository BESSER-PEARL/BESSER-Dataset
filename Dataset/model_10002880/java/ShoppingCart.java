




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class ShoppingCart  {

    private LocalDate creationDate;





    private WebUser webuser;




    private LineItem lineitem;


    public ShoppingCart(
        LocalDate creationDate    ) {
        this.creationDate = creationDate;
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
    public LineItem getLineitem() {
        return lineitem;
    }

    public void setLineitem(LineItem lineitem) {
        this.lineitem = lineitem;
    }

}