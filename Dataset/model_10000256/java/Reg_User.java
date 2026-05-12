





import java.util.List;
import java.util.ArrayList;

public class Reg_User  {

    private String username;
    private String password;
    private String Address;





    private Payment payment;




    private List<Requirement> requirements;


    public Reg_User(
        String username,        String password,        String Address    ) {
        this.username = username;
        this.password = password;
        this.Address = Address;
        this.requirements = new ArrayList<>();
    }

    public Reg_User(
        String username,        String password,        String Address        ArrayList<Requirement> requirements    ) {
        this.username = username;
        this.password = password;
        this.Address = Address;
        this.requirements = requirements;
    }

    public String getUsername() {
        return username;
    }

    public void setUsername(String username) {
        this.username = username;
    }
    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }
    public String getAddress() {
        return Address;
    }

    public void setAddress(String Address) {
        this.Address = Address;
    }

    public Payment getPayment() {
        return payment;
    }

    public void setPayment(Payment payment) {
        this.payment = payment;
    }
    public List<Requirement> getRequirements() {
        return requirements;
    }

    public void addRequirement(Requirement requirement) {
        this.requirements.add(requirement);
    }

}