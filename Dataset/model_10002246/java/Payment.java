





import java.util.List;
import java.util.ArrayList;

public class Payment  {

    private String issuerName;
    private String expiryDate;
    private int amount;
    private int cardNumber;
    private String cardType;





    private List<Volunteer> volunteers;




    private List<Manager> managers;




    private List<Admin> admins;




    private List<Normal_user> normal_users;


    public Payment(
        String issuerName,        String expiryDate,        int amount,        int cardNumber,        String cardType    ) {
        this.issuerName = issuerName;
        this.expiryDate = expiryDate;
        this.amount = amount;
        this.cardNumber = cardNumber;
        this.cardType = cardType;
        this.volunteers = new ArrayList<>();
        this.managers = new ArrayList<>();
        this.admins = new ArrayList<>();
        this.normal_users = new ArrayList<>();
    }

    public Payment(
        String issuerName,        String expiryDate,        int amount,        int cardNumber,        String cardType        ArrayList<Volunteer> volunteers,        ArrayList<Manager> managers,        ArrayList<Admin> admins,        ArrayList<Normal_user> normal_users    ) {
        this.issuerName = issuerName;
        this.expiryDate = expiryDate;
        this.amount = amount;
        this.cardNumber = cardNumber;
        this.cardType = cardType;
        this.volunteers = volunteers;
        this.managers = managers;
        this.admins = admins;
        this.normal_users = normal_users;
    }

    public String getIssuername() {
        return issuerName;
    }

    public void setIssuername(String issuerName) {
        this.issuerName = issuerName;
    }
    public String getExpirydate() {
        return expiryDate;
    }

    public void setExpirydate(String expiryDate) {
        this.expiryDate = expiryDate;
    }
    public int getAmount() {
        return amount;
    }

    public void setAmount(int amount) {
        this.amount = amount;
    }
    public int getCardnumber() {
        return cardNumber;
    }

    public void setCardnumber(int cardNumber) {
        this.cardNumber = cardNumber;
    }
    public String getCardtype() {
        return cardType;
    }

    public void setCardtype(String cardType) {
        this.cardType = cardType;
    }

    public List<Volunteer> getVolunteers() {
        return volunteers;
    }

    public void addVolunteer(Volunteer volunteer) {
        this.volunteers.add(volunteer);
    }
    public List<Manager> getManagers() {
        return managers;
    }

    public void addManager(Manager manager) {
        this.managers.add(manager);
    }
    public List<Admin> getAdmins() {
        return admins;
    }

    public void addAdmin(Admin admin) {
        this.admins.add(admin);
    }
    public List<Normal_user> getNormal_users() {
        return normal_users;
    }

    public void addNormal_user(Normal_user normal_user) {
        this.normal_users.add(normal_user);
    }

}