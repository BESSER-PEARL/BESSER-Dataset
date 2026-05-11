





import java.util.List;
import java.util.ArrayList;

public class Persons_Person  {

    private String fullName;





    private Persons_Community persons_community;


    public Persons_Person(
        String fullName    ) {
        this.fullName = fullName;
    }


    public String getFullname() {
        return fullName;
    }

    public void setFullname(String fullName) {
        this.fullName = fullName;
    }

    public Persons_Community getPersons_community() {
        return persons_community;
    }

    public void setPersons_community(Persons_Community persons_community) {
        this.persons_community = persons_community;
    }

}