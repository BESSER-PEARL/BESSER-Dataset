





import java.util.List;
import java.util.ArrayList;

public class Payment  {

    private String issuerName;
    private int amount;
    private String cardType;
    private String expiryDate;
    private int cardNumber;





    private List<Admin> admins;




    private List<Normal_user> normal_users;




    private List<Volunteer> volunteers;




    private List<SuperAdmin> superadmins;


    public Payment(
        String issuerName,        int amount,        String cardType,        String expiryDate,        int cardNumber    ) {
        this.issuerName = issuerName;
        this.amount = amount;
        this.cardType = cardType;
        this.expiryDate = expiryDate;
        this.cardNumber = cardNumber;
        this.admins = new ArrayList<>();
        this.normal_users = new ArrayList<>();
        this.volunteers = new ArrayList<>();
        this.superadmins = new ArrayList<>();
    }

    public Payment(
        String issuerName,        int amount,        String cardType,        String expiryDate,        int cardNumber        ArrayList<Admin> admins,        ArrayList<Normal_user> normal_users,        ArrayList<Volunteer> volunteers,        ArrayList<SuperAdmin> superadmins    ) {
        this.issuerName = issuerName;
        this.amount = amount;
        this.cardType = cardType;
        this.expiryDate = expiryDate;
        this.cardNumber = cardNumber;
        this.admins = admins;
        this.normal_users = normal_users;
        this.volunteers = volunteers;
        this.superadmins = superadmins;
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