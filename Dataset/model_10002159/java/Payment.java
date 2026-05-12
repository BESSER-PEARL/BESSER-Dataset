





import java.util.List;
import java.util.ArrayList;

public class Payment  {

    private String issuerName;
    private String cardType;
    private int amount;
    private String expiryDate;
    private int cardNumber;





    private List<SuperAdmin> superadmins;




    private List<Normal_user> normal_users;




    private List<Volunteer> volunteers;




    private List<Admin> admins;


    public Payment(
        String issuerName,        String cardType,        int amount,        String expiryDate,        int cardNumber    ) {
        this.issuerName = issuerName;
        this.cardType = cardType;
        this.amount = amount;
        this.expiryDate = expiryDate;
        this.cardNumber = cardNumber;
        this.superadmins = new ArrayList<>();
        this.normal_users = new ArrayList<>();
        this.volunteers = new ArrayList<>();
        this.admins = new ArrayList<>();
    }

    public Payment(
        String issuerName,        String cardType,        int amount,        String expiryDate,        int cardNumber        ArrayList<SuperAdmin> superadmins,        ArrayList<Normal_user> normal_users,        ArrayList<Volunteer> volunteers,        ArrayList<Admin> admins    ) {
        this.issuerName = issuerName;
        this.cardType = cardType;
        this.amount = amount;
        this.expiryDate = expiryDate;
        this.cardNumber = cardNumber;
        this.superadmins = superadmins;
        this.normal_users = normal_users;
        this.volunteers = volunteers;
        this.admins = admins;
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
    public List<Admin> getAdmins() {
        return admins;
    }

    public void addAdmin(Admin admin) {
        this.admins.add(admin);
    }

}