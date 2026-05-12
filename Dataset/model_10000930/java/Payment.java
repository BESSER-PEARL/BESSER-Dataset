





import java.util.List;
import java.util.ArrayList;

public class Payment  {

    private String cardType;
    private int cardNumber;
    private int amount;
    private String issuerName;
    private String expiryDate;





    private List<SuperAdmin> superadmins;




    private List<Admin> admins;




    private List<Volunteer> volunteers;


    public Payment(
        String cardType,        int cardNumber,        int amount,        String issuerName,        String expiryDate    ) {
        this.cardType = cardType;
        this.cardNumber = cardNumber;
        this.amount = amount;
        this.issuerName = issuerName;
        this.expiryDate = expiryDate;
        this.superadmins = new ArrayList<>();
        this.admins = new ArrayList<>();
        this.volunteers = new ArrayList<>();
    }

    public Payment(
        String cardType,        int cardNumber,        int amount,        String issuerName,        String expiryDate        ArrayList<SuperAdmin> superadmins,        ArrayList<Admin> admins,        ArrayList<Volunteer> volunteers    ) {
        this.cardType = cardType;
        this.cardNumber = cardNumber;
        this.amount = amount;
        this.issuerName = issuerName;
        this.expiryDate = expiryDate;
        this.superadmins = superadmins;
        this.admins = admins;
        this.volunteers = volunteers;
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