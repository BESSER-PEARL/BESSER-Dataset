





import java.util.List;
import java.util.ArrayList;

public class shr5_GeldWert  {

    private String wertValue;
    private String verfuegbarkeit;
    private String wert;





    private shr5_ShoppingTransaction shr5_shoppingtransaction;


    public shr5_GeldWert(
        String wertValue,        String verfuegbarkeit,        String wert    ) {
        this.wertValue = wertValue;
        this.verfuegbarkeit = verfuegbarkeit;
        this.wert = wert;
    }


    public String getWertvalue() {
        return wertValue;
    }

    public void setWertvalue(String wertValue) {
        this.wertValue = wertValue;
    }
    public String getVerfuegbarkeit() {
        return verfuegbarkeit;
    }

    public void setVerfuegbarkeit(String verfuegbarkeit) {
        this.verfuegbarkeit = verfuegbarkeit;
    }
    public String getWert() {
        return wert;
    }

    public void setWert(String wert) {
        this.wert = wert;
    }

    public shr5_ShoppingTransaction getShr5_shoppingtransaction() {
        return shr5_shoppingtransaction;
    }

    public void setShr5_shoppingtransaction(shr5_ShoppingTransaction shr5_shoppingtransaction) {
        this.shr5_shoppingtransaction = shr5_shoppingtransaction;
    }

}