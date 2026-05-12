





import java.util.List;
import java.util.ArrayList;

public class Database  {

    private String Details;
    private int income;
    private String service;





    private List<Receptionist> receptionists;




    private Manager manager;


    public Database(
        String Details,        int income,        String service    ) {
        this.Details = Details;
        this.income = income;
        this.service = service;
        this.receptionists = new ArrayList<>();
    }

    public Database(
        String Details,        int income,        String service        ArrayList<Receptionist> receptionists    ) {
        this.Details = Details;
        this.income = income;
        this.service = service;
        this.receptionists = receptionists;
    }

    public String getDetails() {
        return Details;
    }

    public void setDetails(String Details) {
        this.Details = Details;
    }
    public int getIncome() {
        return income;
    }

    public void setIncome(int income) {
        this.income = income;
    }
    public String getService() {
        return service;
    }

    public void setService(String service) {
        this.service = service;
    }

    public List<Receptionist> getReceptionists() {
        return receptionists;
    }

    public void addReceptionist(Receptionist receptionist) {
        this.receptionists.add(receptionist);
    }
    public Manager getManager() {
        return manager;
    }

    public void setManager(Manager manager) {
        this.manager = manager;
    }

}