





import java.util.List;
import java.util.ArrayList;

public class lager  {

    private String bestandZutaten;
    private String attribute;



    public lager(
        String bestandZutaten,        String attribute    ) {
        this.bestandZutaten = bestandZutaten;
        this.attribute = attribute;
    }


    public String getBestandzutaten() {
        return bestandZutaten;
    }

    public void setBestandzutaten(String bestandZutaten) {
        this.bestandZutaten = bestandZutaten;
    }
    public String getAttribute() {
        return attribute;
    }

    public void setAttribute(String attribute) {
        this.attribute = attribute;
    }


}