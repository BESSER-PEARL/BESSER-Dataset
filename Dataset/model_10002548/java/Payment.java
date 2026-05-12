





import java.util.List;
import java.util.ArrayList;

public class Payment  {

    private int cardNumber;
    private String expiryDate;
    private String issuerName;
    private String cardType;
    private int amount;





    private List<Admin> admins;




    private List<SuperAdmin> superadmins;




    private List<Normal_user> normal_users;




    private List<Volunteer> volunteers;


    public Payment(
        int cardNumber,        String expiryDate,        String issuerName,        String cardType,        int amount    ) {
        this.cardNumber = cardNumber;
        this.expiryDate = expiryDate;
        this.issuerName = issuerName;
        this.cardType = cardType;
        this.amount = amount;
        this.admins = new ArrayList<>();
        this.superadmins = new ArrayList<>();
        this.normal_users = new ArrayList<>();
        this.volunteers = new ArrayList<>();
    }

    public Payment(
        int cardNumber,        String expiryDate,        String issuerName,        String cardType,        int amount        ArrayList<Admin> admins,        ArrayList<SuperAdmin> superadmins,        ArrayList<Normal_user> normal_users,        ArrayList<Volunteer> volunteers    ) {
        this.cardNumber = cardNumber;
        this.expiryDate = expiryDate;
        this.issuerName = issuerName;
        this.cardType = cardType;
        this.amount = amount;
        this.admins = admins;
        this.superadmins = superadmins;
        this.normal_users = normal_users;
        this.volunteers = volunteers;
    }

    public int getCardnumber() {
        return cardNumber;
    }

    public void setCardnumber(int cardNumber) {
        this.cardNumber = cardNumber;
    }
    public String getExpirydate() {
        return expiryDate;
    }

    public void setExpirydate(String expiryDate) {
        this.expiryDate = expiryDate;
    }
    public String getIssuername() {
        return issuerName;
    }

    public void setIssuername(String issuerName) {
        this.issuerName = issuerName;
    }
    public String getCardtype() {
        return cardType;
    }

    public void setCardtype(String cardType) {
        this.cardType = cardType;
    }
    public int getAmount() {
        return amount;
    }

    public void setAmount(int amount) {
        this.amount = amount;
    }

    public List<Admin> getAdmins() {
        return admins;
    }

    public void addAdmin(Admin admin) {
        this.admins.add(admin);
    }
    public List<SuperAdmin> getSuperadmins() {
        return superadmins;
    }

    public void addSuperadmin(Superadmin superadmin) {
        this.superadmins.add(superadmin);
    }
    public List<Normal_user> getNormal_users() {
        return normal_users;
    }

    public void addNormal_user(Normal_user normal_user) {
        this.normal_users.add(normal_user);
    }
    public List<Volunteer> getVolunteers() {
        return volunteers;
    }

    public void addVolunteer(Volunteer volunteer) {
        this.volunteers.add(volunteer);
    }

}