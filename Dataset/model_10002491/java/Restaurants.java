





import java.util.List;
import java.util.ArrayList;

public class Restaurants  {

    private int r_ID;
    private String r_name;
    private String r_address;
    private String r_cuisine;
    private int r_contact;





    private Booking booking;




    private List<Table> tables;


    public Restaurants(
        int r_ID,        String r_name,        String r_address,        String r_cuisine,        int r_contact    ) {
        this.r_ID = r_ID;
        this.r_name = r_name;
        this.r_address = r_address;
        this.r_cuisine = r_cuisine;
        this.r_contact = r_contact;
        this.tables = new ArrayList<>();
    }

    public Restaurants(
        int r_ID,        String r_name,        String r_address,        String r_cuisine,        int r_contact        ArrayList<Table> tables    ) {
        this.r_ID = r_ID;
        this.r_name = r_name;
        this.r_address = r_address;
        this.r_cuisine = r_cuisine;
        this.r_contact = r_contact;
        this.tables = tables;
    }

    public int getR_id() {
        return r_ID;
    }

    public void setR_id(int r_ID) {
        this.r_ID = r_ID;
    }
    public String getR_name() {
        return r_name;
    }

    public void setR_name(String r_name) {
        this.r_name = r_name;
    }
    public String getR_address() {
        return r_address;
    }

    public void setR_address(String r_address) {
        this.r_address = r_address;
    }
    public String getR_cuisine() {
        return r_cuisine;
    }

    public void setR_cuisine(String r_cuisine) {
        this.r_cuisine = r_cuisine;
    }
    public int getR_contact() {
        return r_contact;
    }

    public void setR_contact(int r_contact) {
        this.r_contact = r_contact;
    }

    public Booking getBooking() {
        return booking;
    }

    public void setBooking(Booking booking) {
        this.booking = booking;
    }
    public List<Table> getTables() {
        return tables;
    }

    public void addTable(Table table) {
        this.tables.add(table);
    }

}