





import java.util.List;
import java.util.ArrayList;

public class Persons_Association extends NamedElement {






    private Persons_Community persons_community;


    public Persons_Association(
    ) {
        super(
        );
    }



    public Persons_Community getPersons_community() {
        return persons_community;
    }

    public void setPersons_community(Persons_Community persons_community) {
        this.persons_community = persons_community;
    }

}