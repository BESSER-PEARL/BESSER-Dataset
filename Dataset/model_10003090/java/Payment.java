





import java.util.List;
import java.util.ArrayList;

public class Payment  {

    private int cardNumber;
    private String cardType;
    private String issuerName;
    private int amount;
    private String expiryDate;





    private List<SuperAdmin> superadmins;




    private List<Normal_user> normal_users;




    private List<Admin> admins;




    private List<Volunteer> volunteers;


    public Payment(
        int cardNumber,        String cardType,        String issuerName,        int amount,        String expiryDate    ) {
        this.cardNumber = cardNumber;
        this.cardType = cardType;
        this.issuerName = issuerName;
        this.amount = amount;
        this.expiryDate = expiryDate;
        this.superadmins = new ArrayList<>();
        this.normal_users = new ArrayList<>();
        this.admins = new ArrayList<>();
        this.volunteers = new ArrayList<>();
    }

    public Payment(
        int cardNumber,        String cardType,        String issuerName,        int amount,        String expiryDate        ArrayList<SuperAdmin> superadmins,        ArrayList<Normal_user> normal_users,        ArrayList<Admin> admins,        ArrayList<Volunteer> volunteers    ) {
        this.cardNumber = cardNumber;
        this.cardType = cardType;
        this.issuerName = issuerName;
        this.amount = amount;
        this.expiryDate = expiryDate;
        this.superadmins = superadmins;
        this.normal_users = normal_users;
        this.admins = admins;
        this.volunteers = volunteers;
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
    public String getIssuername() {
        return issuerName;
    }

    public void setIssuername(String issuerName) {
        this.issuerName = issuerName;
    }
    public int getAmount() {
        return amount;
    }

    public void setAmount(int amount) {
        this.amount = amount;
    }
    public String getExpirydate() {
        return expiryDate;
    }

    public void setExpirydate(String expiryDate) {
        this.expiryDate = expiryDate;
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
    public List<Admin> getAdmins() {
        return admins;
    }

    public void addAdmin(Admin admin) {
        this.admins.add(admin);
    }
    public List<Volunteer> getVolunteers() {
        return volunteers;
    }

    public void addVolunteer(Volunteer volunteer) {
        this.volunteers.add(volunteer);
    }

}