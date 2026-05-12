





import java.util.List;
import java.util.ArrayList;

public class Products  {

    private int racknumber;
    private int totral;





    private Administrator administrator;




    private Item item;


    public Products(
        int racknumber,        int totral    ) {
        this.racknumber = racknumber;
        this.totral = totral;
    }


    public int getRacknumber() {
        return racknumber;
    }

    public void setRacknumber(int racknumber) {
        this.racknumber = racknumber;
    }
    public int getTotral() {
        return totral;
    }

    public void setTotral(int totral) {
        this.totral = totral;
    }

    public Administrator getAdministrator() {
        return administrator;
    }

    public void setAdministrator(Administrator administrator) {
        this.administrator = administrator;
    }
    public Item getItem() {
        return item;
    }

    public void setItem(Item item) {
        this.item = item;
    }

}