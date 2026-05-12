





import java.util.List;
import java.util.ArrayList;

public class Csutomer  {

    private String register;
    private String id;
    private String attribute;
    private String Adress;
    private String password;
    private String tel_no;
    private String email;
    private String name;





    private menu menu;




    private List<order> orders;


    public Csutomer(
        String register,        String id,        String attribute,        String Adress,        String password,        String tel_no,        String email,        String name    ) {
        this.register = register;
        this.id = id;
        this.attribute = attribute;
        this.Adress = Adress;
        this.password = password;
        this.tel_no = tel_no;
        this.email = email;
        this.name = name;
        this.orders = new ArrayList<>();
    }

    public Csutomer(
        String register,        String id,        String attribute,        String Adress,        String password,        String tel_no,        String email,        String name        ArrayList<order> orders    ) {
        this.register = register;
        this.id = id;
        this.attribute = attribute;
        this.Adress = Adress;
        this.password = password;
        this.tel_no = tel_no;
        this.email = email;
        this.name = name;
        this.orders = orders;
    }

    public String getRegister() {
        return register;
    }

    public void setRegister(String register) {
        this.register = register;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getAttribute() {
        return attribute;
    }

    public void setAttribute(String attribute) {
        this.attribute = attribute;
    }
    public String getAdress() {
        return Adress;
    }

    public void setAdress(String Adress) {
        this.Adress = Adress;
    }
    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }
    public String getTel_no() {
        return tel_no;
    }

    public void setTel_no(String tel_no) {
        this.tel_no = tel_no;
    }
    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public menu getMenu() {
        return menu;
    }

    public void setMenu(menu menu) {
        this.menu = menu;
    }
    public List<order> getOrders() {
        return orders;
    }

    public void addOrder(Order order) {
        this.orders.add(order);
    }

}