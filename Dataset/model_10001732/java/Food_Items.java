





import java.util.List;
import java.util.ArrayList;

public class Food_Items  {

    private String Item_Name;
    private int Items_ID;
    private String item_photo;
    private int Items_Price;
    private String Items_Detail;
    private None Items_Manage;





    private List<Customer> customers;




    private Admin admin;


    public Food_Items(
        String Item_Name,        int Items_ID,        String item_photo,        int Items_Price,        String Items_Detail,        None Items_Manage    ) {
        this.Item_Name = Item_Name;
        this.Items_ID = Items_ID;
        this.item_photo = item_photo;
        this.Items_Price = Items_Price;
        this.Items_Detail = Items_Detail;
        this.Items_Manage = Items_Manage;
        this.customers = new ArrayList<>();
    }

    public Food_Items(
        String Item_Name,        int Items_ID,        String item_photo,        int Items_Price,        String Items_Detail,        None Items_Manage        ArrayList<Customer> customers    ) {
        this.Item_Name = Item_Name;
        this.Items_ID = Items_ID;
        this.item_photo = item_photo;
        this.Items_Price = Items_Price;
        this.Items_Detail = Items_Detail;
        this.Items_Manage = Items_Manage;
        this.customers = customers;
    }

    public String getItem_name() {
        return Item_Name;
    }

    public void setItem_name(String Item_Name) {
        this.Item_Name = Item_Name;
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
    public None getItems_manage() {
        return Items_Manage;
    }

    public void setItems_manage(None Items_Manage) {
        this.Items_Manage = Items_Manage;
    }

    public List<Customer> getCustomers() {
        return customers;
    }

    public void addCustomer(Customer customer) {
        this.customers.add(customer);
    }
    public Admin getAdmin() {
        return admin;
    }

    public void setAdmin(Admin admin) {
        this.admin = admin;
    }

}