





import java.util.List;
import java.util.ArrayList;

public class personDsl_Person  {

    private int ID;
    private String name;





    private personDsl_PersonContainer persondsl_personcontainer;


    public personDsl_Person(
        int ID,        String name    ) {
        this.ID = ID;
        this.name = name;
    }


    public int getId() {
        return ID;
    }

    public void setId(int ID) {
        this.ID = ID;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public personDsl_PersonContainer getPersondsl_personcontainer() {
        return persondsl_personcontainer;
    }

    public void setPersondsl_personcontainer(personDsl_PersonContainer persondsl_personcontainer) {
        this.persondsl_personcontainer = persondsl_personcontainer;
    }

}