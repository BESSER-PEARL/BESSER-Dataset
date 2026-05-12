





import java.util.List;
import java.util.ArrayList;

public class Payment  {

    private String cardType;
    private String issuerName;
    private int amount;
    private int cardNumber;
    private String expiryDate;





    private List<Normal_user> normal_users;




    private List<Volunteer> volunteers;




    private List<SuperAdmin> superadmins;




    private List<Admin> admins;


    public Payment(
        String cardType,        String issuerName,        int amount,        int cardNumber,        String expiryDate    ) {
        this.cardType = cardType;
        this.issuerName = issuerName;
        this.amount = amount;
        this.cardNumber = cardNumber;
        this.expiryDate = expiryDate;
        this.normal_users = new ArrayList<>();
        this.volunteers = new ArrayList<>();
        this.superadmins = new ArrayList<>();
        this.admins = new ArrayList<>();
    }

    public Payment(
        String cardType,        String issuerName,        int amount,        int cardNumber,        String expiryDate        ArrayList<Normal_user> normal_users,        ArrayList<Volunteer> volunteers,        ArrayList<SuperAdmin> superadmins,        ArrayList<Admin> admins    ) {
        this.cardType = cardType;
        this.issuerName = issuerName;
        this.amount = amount;
        this.cardNumber = cardNumber;
        this.expiryDate = expiryDate;
        this.normal_users = normal_users;
        this.volunteers = volunteers;
        this.superadmins = superadmins;
        this.admins = admins;
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