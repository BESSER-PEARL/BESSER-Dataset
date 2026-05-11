





import java.util.List;
import java.util.ArrayList;

public class Persons_Person  {

    private String name;
    private int ID;





    private Persons_PersonContainer persons_personcontainer;


    public Persons_Person(
        String name,        int ID    ) {
        this.name = name;
        this.ID = ID;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public int getId() {
        return ID;
    }

    public void setId(int ID) {
        this.ID = ID;
    }

    public Persons_PersonContainer getPersons_personcontainer() {
        return persons_personcontainer;
    }

    public void setPersons_personcontainer(Persons_PersonContainer persons_personcontainer) {
        this.persons_personcontainer = persons_personcontainer;
    }

}