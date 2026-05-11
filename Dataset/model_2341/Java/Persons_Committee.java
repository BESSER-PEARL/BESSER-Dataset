





import java.util.List;
import java.util.ArrayList;

public class Persons_Committee extends NamedElement {






    private Persons_Association persons_association;




    private Persons_TownHall persons_townhall;


    public Persons_Committee(
    ) {
        super(
        );
    }



    public Persons_Association getPersons_association() {
        return persons_association;
    }

    public void setPersons_association(Persons_Association persons_association) {
        this.persons_association = persons_association;
    }
    public Persons_TownHall getPersons_townhall() {
        return persons_townhall;
    }

    public void setPersons_townhall(Persons_TownHall persons_townhall) {
        this.persons_townhall = persons_townhall;
    }

}