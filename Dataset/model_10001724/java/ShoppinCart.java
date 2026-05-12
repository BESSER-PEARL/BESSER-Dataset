




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class ShoppinCart  {

    private LocalDate creationDate;





    private ShoppinCart shoppincart;


    public ShoppinCart(
        LocalDate creationDate    ) {
        this.creationDate = creationDate;
    }


    public LocalDate getCreationdate() {
        return creationDate;
    }

    public void setCreationdate(LocalDate creationDate) {
        this.creationDate = creationDate;
    }

    public ShoppinCart getShoppincart() {
        return shoppincart;
    }

    public void setShoppincart(ShoppinCart shoppincart) {
        this.shoppincart = shoppincart;
    }

}