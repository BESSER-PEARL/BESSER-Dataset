





import java.util.List;
import java.util.ArrayList;

public class Payment  {

    private String cardType;
    private int cardNumber;
    private String expiryDate;
    private int amount;
    private String issuerName;





    private List<Volunteer> volunteers;




    private List<SuperAdmin> superadmins;




    private List<Normal_user> normal_users;




    private List<Admin> admins;


    public Payment(
        String cardType,        int cardNumber,        String expiryDate,        int amount,        String issuerName    ) {
        this.cardType = cardType;
        this.cardNumber = cardNumber;
        this.expiryDate = expiryDate;
        this.amount = amount;
        this.issuerName = issuerName;
        this.volunteers = new ArrayList<>();
        this.superadmins = new ArrayList<>();
        this.normal_users = new ArrayList<>();
        this.admins = new ArrayList<>();
    }

    public Payment(
        String cardType,        int cardNumber,        String expiryDate,        int amount,        String issuerName        ArrayList<Volunteer> volunteers,        ArrayList<SuperAdmin> superadmins,        ArrayList<Normal_user> normal_users,        ArrayList<Admin> admins    ) {
        this.cardType = cardType;
        this.cardNumber = cardNumber;
        this.expiryDate = expiryDate;
        this.amount = amount;
        this.issuerName = issuerName;
        this.volunteers = volunteers;
        this.superadmins = superadmins;
        this.normal_users = normal_users;
        this.admins = admins;
    }

    public String getCardtype() {
        return cardType;
    }

    public void setCardtype(String cardType) {
        this.cardType = cardType;
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
    public int getAmount() {
        return amount;
    }

    public void setAmount(int amount) {
        this.amount = amount;
    }
    public String getIssuername() {
        return issuerName;
    }

    public void setIssuername(String issuerName) {
        this.issuerName = issuerName;
    }

    public List<Volunteer> getVolunteers() {
        return volunteers;
    }

    public void addVolunteer(Volunteer volunteer) {
        this.volunteers.add(volunteer);
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

}