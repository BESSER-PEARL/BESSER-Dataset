





import java.util.List;
import java.util.ArrayList;

public class Classes_Restaurants_RestaurantTable  {

    private String numberOfSeats;
    private String tableNumber;



    public Classes_Restaurants_RestaurantTable(
        String numberOfSeats,        String tableNumber    ) {
        this.numberOfSeats = numberOfSeats;
        this.tableNumber = tableNumber;
    }


    public String getNumberofseats() {
        return numberOfSeats;
    }

    public void setNumberofseats(String numberOfSeats) {
        this.numberOfSeats = numberOfSeats;
    }
    public String getTablenumber() {
        return tableNumber;
    }

    public void setTablenumber(String tableNumber) {
        this.tableNumber = tableNumber;
    }


}