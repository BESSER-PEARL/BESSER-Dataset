





import java.util.List;
import java.util.ArrayList;

public class fair_Class  {

    private String comments;
    private String name;





    private List<fair_Lot> fair_lots;




    private fair_Lot fair_lot;




    private fair_Department fair_department;




    private fair_Department fair_department;




    private List<fair_Person> fair_persons;


    public fair_Class(
        String comments,        String name    ) {
        this.comments = comments;
        this.name = name;
        this.fair_lots = new ArrayList<>();
        this.fair_persons = new ArrayList<>();
    }

    public fair_Class(
        String comments,        String name        ArrayList<fair_Lot> fair_lots,        ArrayList<fair_Person> fair_persons    ) {
        this.comments = comments;
        this.name = name;
        this.fair_lots = fair_lots;
        this.fair_persons = fair_persons;
    }

    public String getComments() {
        return comments;
    }

    public void setComments(String comments) {
        this.comments = comments;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<fair_Lot> getFair_lots() {
        return fair_lots;
    }

    public void addFair_lot(Fair_lot fair_lot) {
        this.fair_lots.add(fair_lot);
    }
    public fair_Lot getFair_lot() {
        return fair_lot;
    }

    public void setFair_lot(fair_Lot fair_lot) {
        this.fair_lot = fair_lot;
    }
    public fair_Department getFair_department() {
        return fair_department;
    }

    public void setFair_department(fair_Department fair_department) {
        this.fair_department = fair_department;
    }
    public fair_Department getFair_department() {
        return fair_department;
    }

    public void setFair_department(fair_Department fair_department) {
        this.fair_department = fair_department;
    }
    public List<fair_Person> getFair_persons() {
        return fair_persons;
    }

    public void addFair_person(Fair_person fair_person) {
        this.fair_persons.add(fair_person);
    }

}