





import java.util.List;
import java.util.ArrayList;

public class online_shopping_Session_manager  {

    private None Department_Name;
    private None Person_ID;





    private online_shopping_Person online_shopping_person;




    private online_shopping_Deoartment online_shopping_deoartment;


    public online_shopping_Session_manager(
        None Department_Name,        None Person_ID    ) {
        this.Department_Name = Department_Name;
        this.Person_ID = Person_ID;
    }


    public None getDepartment_name() {
        return Department_Name;
    }

    public void setDepartment_name(None Department_Name) {
        this.Department_Name = Department_Name;
    }
    public None getPerson_id() {
        return Person_ID;
    }

    public void setPerson_id(None Person_ID) {
        this.Person_ID = Person_ID;
    }

    public online_shopping_Person getOnline_shopping_person() {
        return online_shopping_person;
    }

    public void setOnline_shopping_person(online_shopping_Person online_shopping_person) {
        this.online_shopping_person = online_shopping_person;
    }
    public online_shopping_Deoartment getOnline_shopping_deoartment() {
        return online_shopping_deoartment;
    }

    public void setOnline_shopping_deoartment(online_shopping_Deoartment online_shopping_deoartment) {
        this.online_shopping_deoartment = online_shopping_deoartment;
    }

}