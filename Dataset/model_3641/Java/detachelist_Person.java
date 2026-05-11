





import java.util.List;
import java.util.ArrayList;

public class detachelist_Person  {

    private String name;





    private detachelist_Contacts detachelist_contacts;




    private detachelist_Person detachelist_person;




    private detachelist_Contacts detachelist_contacts;


    public detachelist_Person(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public detachelist_Contacts getDetachelist_contacts() {
        return detachelist_contacts;
    }

    public void setDetachelist_contacts(detachelist_Contacts detachelist_contacts) {
        this.detachelist_contacts = detachelist_contacts;
    }
    public detachelist_Person getDetachelist_person() {
        return detachelist_person;
    }

    public void setDetachelist_person(detachelist_Person detachelist_person) {
        this.detachelist_person = detachelist_person;
    }
    public detachelist_Contacts getDetachelist_contacts() {
        return detachelist_contacts;
    }

    public void setDetachelist_contacts(detachelist_Contacts detachelist_contacts) {
        this.detachelist_contacts = detachelist_contacts;
    }

}