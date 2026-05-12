





import java.util.List;
import java.util.ArrayList;

public class model_Transaction  {

    private None date;
    private float ammount;



    public model_Transaction(
        None date,        float ammount    ) {
        this.date = date;
        this.ammount = ammount;
    }


    public None getDate() {
        return date;
    }

    public void setDate(None date) {
        this.date = date;
    }
    public float getAmmount() {
        return ammount;
    }

    public void setAmmount(float ammount) {
        this.ammount = ammount;
    }


}