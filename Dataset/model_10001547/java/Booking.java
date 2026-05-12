





import java.util.List;
import java.util.ArrayList;

public class Booking  {

    private String customer_name;
    private int arrival_time;
    private int table_number;





    private Table table;


    public Booking(
        String customer_name,        int arrival_time,        int table_number    ) {
        this.customer_name = customer_name;
        this.arrival_time = arrival_time;
        this.table_number = table_number;
    }


    public String getCustomer_name() {
        return customer_name;
    }

    public void setCustomer_name(String customer_name) {
        this.customer_name = customer_name;
    }
    public int getArrival_time() {
        return arrival_time;
    }

    public void setArrival_time(int arrival_time) {
        this.arrival_time = arrival_time;
    }
    public int getTable_number() {
        return table_number;
    }

    public void setTable_number(int table_number) {
        this.table_number = table_number;
    }

    public Table getTable() {
        return table;
    }

    public void setTable(Table table) {
        this.table = table;
    }

}