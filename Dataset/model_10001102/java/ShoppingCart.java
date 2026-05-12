




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class ShoppingCart  {

    private String Addcartitem;
    private LocalDate creationDate;
    private String UpdateCartDetails;



    public ShoppingCart(
        String Addcartitem,        LocalDate creationDate,        String UpdateCartDetails    ) {
        this.Addcartitem = Addcartitem;
        this.creationDate = creationDate;
        this.UpdateCartDetails = UpdateCartDetails;
    }


    public String getAddcartitem() {
        return Addcartitem;
    }

    public void setAddcartitem(String Addcartitem) {
        this.Addcartitem = Addcartitem;
    }
    public LocalDate getCreationdate() {
        return creationDate;
    }

    public void setCreationdate(LocalDate creationDate) {
        this.creationDate = creationDate;
    }
    public String getUpdatecartdetails() {
        return UpdateCartDetails;
    }

    public void setUpdatecartdetails(String UpdateCartDetails) {
        this.UpdateCartDetails = UpdateCartDetails;
    }


}