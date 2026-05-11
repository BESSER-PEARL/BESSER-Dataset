





import java.util.List;
import java.util.ArrayList;

public class persons_District extends NamedElement {






    private List<persons_Facility> persons_facilitys;




    private persons_TownHall persons_townhall;


    public persons_District(
    ) {
        super(
        );
        this.persons_facilitys = new ArrayList<>();
    }

    public persons_District(
        ArrayList<persons_Facility> persons_facilitys    ) {
        this.persons_facilitys = persons_facilitys;
    }


    public List<persons_Facility> getPersons_facilitys() {
        return persons_facilitys;
    }

    public void addPersons_facility(Persons_facility persons_facility) {
        this.persons_facilitys.add(persons_facility);
    }
    public persons_TownHall getPersons_townhall() {
        return persons_townhall;
    }

    public void setPersons_townhall(persons_TownHall persons_townhall) {
        this.persons_townhall = persons_townhall;
    }

}