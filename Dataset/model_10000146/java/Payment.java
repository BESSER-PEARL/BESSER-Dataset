





import java.util.List;
import java.util.ArrayList;

public class Payment  {

    private int amount;
    private String issuerName;
    private String cardType;
    private String expiryDate;
    private int cardNumber;





    private List<SuperAdmin> superadmins;




    private List<Volunteer> volunteers;




    private List<Normal_user> normal_users;




    private List<Admin> admins;


    public Payment(
        int amount,        String issuerName,        String cardType,        String expiryDate,        int cardNumber    ) {
        this.amount = amount;
        this.issuerName = issuerName;
        this.cardType = cardType;
        this.expiryDate = expiryDate;
        this.cardNumber = cardNumber;
        this.superadmins = new ArrayList<>();
        this.volunteers = new ArrayList<>();
        this.normal_users = new ArrayList<>();
        this.admins = new ArrayList<>();
    }

    public Payment(
        int amount,        String issuerName,        String cardType,        String expiryDate,        int cardNumber        ArrayList<SuperAdmin> superadmins,        ArrayList<Volunteer> volunteers,        ArrayList<Normal_user> normal_users,        ArrayList<Admin> admins    ) {
        this.amount = amount;
        this.issuerName = issuerName;
        this.cardType = cardType;
        this.expiryDate = expiryDate;
        this.cardNumber = cardNumber;
        this.superadmins = superadmins;
        this.volunteers = volunteers;
        this.normal_users = normal_users;
        this.admins = admins;
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

    public List<SuperAdmin> getSuperadmins() {
        return superadmins;
    }

    public void addSuperadmin(Superadmin superadmin) {
        this.superadmins.add(superadmin);
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
    public List<Admin> getAdmins() {
        return admins;
    }

    public void addAdmin(Admin admin) {
        this.admins.add(admin);
    }

}