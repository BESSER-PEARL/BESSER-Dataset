





import java.util.List;
import java.util.ArrayList;

public class Payment  {

    private int amount;
    private String cardType;
    private String expiryDate;
    private int cardNumber;
    private String issuerName;





    private List<Volunteer> volunteers;




    private List<Normal_user> normal_users;




    private List<SuperAdmin> superadmins;




    private List<Admin> admins;


    public Payment(
        int amount,        String cardType,        String expiryDate,        int cardNumber,        String issuerName    ) {
        this.amount = amount;
        this.cardType = cardType;
        this.expiryDate = expiryDate;
        this.cardNumber = cardNumber;
        this.issuerName = issuerName;
        this.volunteers = new ArrayList<>();
        this.normal_users = new ArrayList<>();
        this.superadmins = new ArrayList<>();
        this.admins = new ArrayList<>();
    }

    public Payment(
        int amount,        String cardType,        String expiryDate,        int cardNumber,        String issuerName        ArrayList<Volunteer> volunteers,        ArrayList<Normal_user> normal_users,        ArrayList<SuperAdmin> superadmins,        ArrayList<Admin> admins    ) {
        this.amount = amount;
        this.cardType = cardType;
        this.expiryDate = expiryDate;
        this.cardNumber = cardNumber;
        this.issuerName = issuerName;
        this.volunteers = volunteers;
        this.normal_users = normal_users;
        this.superadmins = superadmins;
        this.admins = admins;
    }

    public int getAmount() {
        return amount;
    }

    public void setAmount(int amount) {
        this.amount = amount;
    }
    public String getCardtype() {
        return cardType;
    }

    public void setCardtype(String cardType) {
        this.cardType = cardType;
    }
    public String getExpirydate() {
        return expiryDate;
    }

    public void setExpirydate(String expiryDate) {
        this.expiryDate = expiryDate;
    }
    public int getCardnumber() {
        return cardNumber;
    }

    public void setCardnumber(int cardNumber) {
        this.cardNumber = cardNumber;
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
    public List<Normal_user> getNormal_users() {
        return normal_users;
    }

    public void addNormal_user(Normal_user normal_user) {
        this.normal_users.add(normal_user);
    }
    public List<SuperAdmin> getSuperadmins() {
        return superadmins;
    }

    public void addSuperadmin(Superadmin superadmin) {
        this.superadmins.add(superadmin);
    }
    public List<Admin> getAdmins() {
        return admins;
    }

    public void addAdmin(Admin admin) {
        this.admins.add(admin);
    }

}