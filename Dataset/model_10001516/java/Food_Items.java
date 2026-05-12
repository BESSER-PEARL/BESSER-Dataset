





import java.util.List;
import java.util.ArrayList;

public class Food_Items  {

    private int Items_ID;
    private String item_photo;
    private String Item_Name;
    private None Items_Manage;
    private int Items_Price;
    private String Items_Detail;





    private List<Customer> customers;


    public Food_Items(
        int Items_ID,        String item_photo,        String Item_Name,        None Items_Manage,        int Items_Price,        String Items_Detail    ) {
        this.Items_ID = Items_ID;
        this.item_photo = item_photo;
        this.Item_Name = Item_Name;
        this.Items_Manage = Items_Manage;
        this.Items_Price = Items_Price;
        this.Items_Detail = Items_Detail;
        this.customers = new ArrayList<>();
    }

    public Food_Items(
        int Items_ID,        String item_photo,        String Item_Name,        None Items_Manage,        int Items_Price,        String Items_Detail        ArrayList<Customer> customers    ) {
        this.Items_ID = Items_ID;
        this.item_photo = item_photo;
        this.Item_Name = Item_Name;
        this.Items_Manage = Items_Manage;
        this.Items_Price = Items_Price;
        this.Items_Detail = Items_Detail;
        this.customers = customers;
    }

    public int getItems_id() {
        return Items_ID;
    }

    public void setItems_id(int Items_ID) {
        this.Items_ID = Items_ID;
    }
    public String getItem_photo() {
        return item_photo;
    }

    public void setItem_photo(String item_photo) {
        this.item_photo = item_photo;
    }
    public String getItem_name() {
        return Item_Name;
    }

    public void setItem_name(String Item_Name) {
        this.Item_Name = Item_Name;
    }
    public None getItems_manage() {
        return Items_Manage;
    }

    public void setItems_manage(None Items_Manage) {
        this.Items_Manage = Items_Manage;
    }
    public int getItems_price() {
        return Items_Price;
    }

    public void setItems_price(int Items_Price) {
        this.Items_Price = Items_Price;
    }
    public String getItems_detail() {
        return Items_Detail;
    }

    public void setItems_detail(String Items_Detail) {
        this.Items_Detail = Items_Detail;
    }

    public List<Customer> getCustomers() {
        return customers;
    }

    public void addCustomer(Customer customer) {
        this.customers.add(customer);
    }

}