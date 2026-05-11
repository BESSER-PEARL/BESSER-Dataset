





import java.util.List;
import java.util.ArrayList;

public class persons_Association extends NamedElement {






    private persons_Community persons_community;




    private persons_Committee persons_committee;


    public persons_Association(
    ) {
        super(
        );
    }



    public persons_Community getPersons_community() {
        return persons_community;
    }

    public void setPersons_community(persons_Community persons_community) {
        this.persons_community = persons_community;
    }
    public persons_Committee getPersons_committee() {
        return persons_committee;
    }

    public void setPersons_committee(persons_Committee persons_committee) {
        this.persons_committee = persons_committee;
    }

}