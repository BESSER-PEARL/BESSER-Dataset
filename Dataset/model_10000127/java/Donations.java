





import java.util.List;
import java.util.ArrayList;

public class Donations  {

    private String cardType;
    private int expirationDate;
    private int cardNumber;
    private int amount;
    private String issuerName;





    private List<Volunteer> volunteers;




    private List<Admin> admins;




    private List<Executive_Director> executive_directors;




    private List<Normal_user> normal_users;


    public Donations(
        String cardType,        int expirationDate,        int cardNumber,        int amount,        String issuerName    ) {
        this.cardType = cardType;
        this.expirationDate = expirationDate;
        this.cardNumber = cardNumber;
        this.amount = amount;
        this.issuerName = issuerName;
        this.volunteers = new ArrayList<>();
        this.admins = new ArrayList<>();
        this.executive_directors = new ArrayList<>();
        this.normal_users = new ArrayList<>();
    }

    public Donations(
        String cardType,        int expirationDate,        int cardNumber,        int amount,        String issuerName        ArrayList<Volunteer> volunteers,        ArrayList<Admin> admins,        ArrayList<Executive_Director> executive_directors,        ArrayList<Normal_user> normal_users    ) {
        this.cardType = cardType;
        this.expirationDate = expirationDate;
        this.cardNumber = cardNumber;
        this.amount = amount;
        this.issuerName = issuerName;
        this.volunteers = volunteers;
        this.admins = admins;
        this.executive_directors = executive_directors;
        this.normal_users = normal_users;
    }

    public String getCardtype() {
        return cardType;
    }

    public void setCardtype(String cardType) {
        this.cardType = cardType;
    }
    public int getExpirationdate() {
        return expirationDate;
    }

    public void setExpirationdate(int expirationDate) {
        this.expirationDate = expirationDate;
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
    public List<Executive_Director> getExecutive_directors() {
        return executive_directors;
    }

    public void addExecutive_director(Executive_director executive_director) {
        this.executive_directors.add(executive_director);
    }
    public List<Normal_user> getNormal_users() {
        return normal_users;
    }

    public void addNormal_user(Normal_user normal_user) {
        this.normal_users.add(normal_user);
    }

}