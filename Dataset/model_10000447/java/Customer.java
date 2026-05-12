





import java.util.List;
import java.util.ArrayList;

public class Customer  {

    private int numberPeople;
    private String name;



    public Customer(
        int numberPeople,        String name    ) {
        this.numberPeople = numberPeople;
        this.name = name;
    }


    public int getNumberpeople() {
        return numberPeople;
    }

    public void setNumberpeople(int numberPeople) {
        this.numberPeople = numberPeople;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}