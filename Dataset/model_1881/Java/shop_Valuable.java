




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class shop_Valuable  {

    private LocalDate date;
    private float value;



    public shop_Valuable(
        LocalDate date,        float value    ) {
        this.date = date;
        this.value = value;
    }


    public LocalDate getDate() {
        return date;
    }

    public void setDate(LocalDate date) {
        this.date = date;
    }
    public float getValue() {
        return value;
    }

    public void setValue(float value) {
        this.value = value;
    }


}