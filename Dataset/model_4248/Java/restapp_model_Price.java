




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class restapp_model_Price  {

    private int id;
    private float value;
    private LocalDate date;



    public restapp_model_Price(
        int id,        float value,        LocalDate date    ) {
        this.id = id;
        this.value = value;
        this.date = date;
    }


    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
    public float getValue() {
        return value;
    }

    public void setValue(float value) {
        this.value = value;
    }
    public LocalDate getDate() {
        return date;
    }

    public void setDate(LocalDate date) {
        this.date = date;
    }


}