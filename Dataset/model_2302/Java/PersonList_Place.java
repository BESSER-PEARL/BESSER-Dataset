





import java.util.List;
import java.util.ArrayList;

public class PersonList_Place  {

    private String address;





    private PersonList_List personlist_list;


    public PersonList_Place(
        String address    ) {
        this.address = address;
    }


    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }

    public PersonList_List getPersonlist_list() {
        return personlist_list;
    }

    public void setPersonlist_list(PersonList_List personlist_list) {
        this.personlist_list = personlist_list;
    }

}