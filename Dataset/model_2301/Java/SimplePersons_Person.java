





import java.util.List;
import java.util.ArrayList;

public class SimplePersons_Person  {

    private String name;





    private SimplePersons_PersonRegister simplepersons_personregister;


    public SimplePersons_Person(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public SimplePersons_PersonRegister getSimplepersons_personregister() {
        return simplepersons_personregister;
    }

    public void setSimplepersons_personregister(SimplePersons_PersonRegister simplepersons_personregister) {
        this.simplepersons_personregister = simplepersons_personregister;
    }

}