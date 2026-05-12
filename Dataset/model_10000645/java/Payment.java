





import java.util.List;
import java.util.ArrayList;

public class Payment  {

    private int amount;
    private String cardType;
    private String expiryDate;
    private String issuerName;
    private int cardNumber;





    private List<Normal_user> normal_users;




    private List<Admin> admins;




    private List<Volunteer> volunteers;




    private List<SuperAdmin> superadmins;


    public Payment(
        int amount,        String cardType,        String expiryDate,        String issuerName,        int cardNumber    ) {
        this.amount = amount;
        this.cardType = cardType;
        this.expiryDate = expiryDate;
        this.issuerName = issuerName;
        this.cardNumber = cardNumber;
        this.normal_users = new ArrayList<>();
        this.admins = new ArrayList<>();
        this.volunteers = new ArrayList<>();
        this.superadmins = new ArrayList<>();
    }

    public Payment(
        int amount,        String cardType,        String expiryDate,        String issuerName,        int cardNumber        ArrayList<Normal_user> normal_users,        ArrayList<Admin> admins,        ArrayList<Volunteer> volunteers,        ArrayList<SuperAdmin> superadmins    ) {
        this.amount = amount;
        this.cardType = cardType;
        this.expiryDate = expiryDate;
        this.issuerName = issuerName;
        this.cardNumber = cardNumber;
        this.normal_users = normal_users;
        this.admins = admins;
        this.volunteers = volunteers;
        this.superadmins = superadmins;
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
    public String getIssuername() {
        return issuerName;
    }

    public void setIssuername(String issuerName) {
        this.issuerName = issuerName;
    }
    public int getCardnumber() {
        return cardNumber;
    }

    public void setCardnumber(int cardNumber) {
        this.cardNumber = cardNumber;
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
    public List<SuperAdmin> getSuperadmins() {
        return superadmins;
    }

    public void addSuperadmin(Superadmin superadmin) {
        this.superadmins.add(superadmin);
    }

}