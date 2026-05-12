





import java.util.List;
import java.util.ArrayList;

public class Products  {

    private int totral;
    private int racknumber;





    private Item item;




    private Administrator administrator;


    public Products(
        int totral,        int racknumber    ) {
        this.totral = totral;
        this.racknumber = racknumber;
    }


    public int getTotral() {
        return totral;
    }

    public void setTotral(int totral) {
        this.totral = totral;
    }
    public int getRacknumber() {
        return racknumber;
    }

    public void setRacknumber(int racknumber) {
        this.racknumber = racknumber;
    }

    public Item getItem() {
        return item;
    }

    public void setItem(Item item) {
        this.item = item;
    }
    public Administrator getAdministrator() {
        return administrator;
    }

    public void setAdministrator(Administrator administrator) {
        this.administrator = administrator;
    }

}