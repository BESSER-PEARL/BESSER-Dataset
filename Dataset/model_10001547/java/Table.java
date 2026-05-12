





import java.util.List;
import java.util.ArrayList;

public class Table  {

    private int table_number;
    private int total_person;





    private Restaurant restaurant;


    public Table(
        int table_number,        int total_person    ) {
        this.table_number = table_number;
        this.total_person = total_person;
    }


    public int getTable_number() {
        return table_number;
    }

    public void setTable_number(int table_number) {
        this.table_number = table_number;
    }
    public int getTotal_person() {
        return total_person;
    }

    public void setTotal_person(int total_person) {
        this.total_person = total_person;
    }

    public Restaurant getRestaurant() {
        return restaurant;
    }

    public void setRestaurant(Restaurant restaurant) {
        this.restaurant = restaurant;
    }

}