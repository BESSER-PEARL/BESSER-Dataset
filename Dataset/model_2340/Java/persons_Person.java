





import java.util.List;
import java.util.ArrayList;

public class persons_Person  {

    private String fullName;





    private persons_Community persons_community;


    public persons_Person(
        String fullName    ) {
        this.fullName = fullName;
    }


    public String getFullname() {
        return fullName;
    }

    public void setFullname(String fullName) {
        this.fullName = fullName;
    }

    public persons_Community getPersons_community() {
        return persons_community;
    }

    public void setPersons_community(persons_Community persons_community) {
        this.persons_community = persons_community;
    }

}