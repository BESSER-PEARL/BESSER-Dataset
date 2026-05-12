





import java.util.List;
import java.util.ArrayList;

public class Payment  {

    private String ex_date;
    private String pay_amount;
    private String pay_mode;
    private String card_no;
    private int pay_id;





    private List<Reg_User> reg_users;




    private List<Property> propertys;


    public Payment(
        String ex_date,        String pay_amount,        String pay_mode,        String card_no,        int pay_id    ) {
        this.ex_date = ex_date;
        this.pay_amount = pay_amount;
        this.pay_mode = pay_mode;
        this.card_no = card_no;
        this.pay_id = pay_id;
        this.reg_users = new ArrayList<>();
        this.propertys = new ArrayList<>();
    }

    public Payment(
        String ex_date,        String pay_amount,        String pay_mode,        String card_no,        int pay_id        ArrayList<Reg_User> reg_users,        ArrayList<Property> propertys    ) {
        this.ex_date = ex_date;
        this.pay_amount = pay_amount;
        this.pay_mode = pay_mode;
        this.card_no = card_no;
        this.pay_id = pay_id;
        this.reg_users = reg_users;
        this.propertys = propertys;
    }

    public String getEx_date() {
        return ex_date;
    }

    public void setEx_date(String ex_date) {
        this.ex_date = ex_date;
    }
    public String getPay_amount() {
        return pay_amount;
    }

    public void setPay_amount(String pay_amount) {
        this.pay_amount = pay_amount;
    }
    public String getPay_mode() {
        return pay_mode;
    }

    public void setPay_mode(String pay_mode) {
        this.pay_mode = pay_mode;
    }
    public String getCard_no() {
        return card_no;
    }

    public void setCard_no(String card_no) {
        this.card_no = card_no;
    }
    public int getPay_id() {
        return pay_id;
    }

    public void setPay_id(int pay_id) {
        this.pay_id = pay_id;
    }

    public List<Reg_User> getReg_users() {
        return reg_users;
    }

    public void addReg_user(Reg_user reg_user) {
        this.reg_users.add(reg_user);
    }
    public List<Property> getPropertys() {
        return propertys;
    }

    public void addProperty(Property property) {
        this.propertys.add(property);
    }

}