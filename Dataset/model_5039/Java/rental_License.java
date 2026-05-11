




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class rental_License  {

    private int number;
    private LocalDate validityDate;



    public rental_License(
        int number,        LocalDate validityDate    ) {
        this.number = number;
        this.validityDate = validityDate;
    }


    public int getNumber() {
        return number;
    }

    public void setNumber(int number) {
        this.number = number;
    }
    public LocalDate getValiditydate() {
        return validityDate;
    }

    public void setValiditydate(LocalDate validityDate) {
        this.validityDate = validityDate;
    }


}