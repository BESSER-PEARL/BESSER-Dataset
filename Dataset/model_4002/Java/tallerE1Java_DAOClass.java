





import java.util.List;
import java.util.ArrayList;

public class tallerE1Java_DAOClass extends Class {






    private List<tallerE1Java_EntityClass> tallere1java_entityclasss;


    public tallerE1Java_DAOClass(
    ) {
        super(
        );
        this.tallere1java_entityclasss = new ArrayList<>();
    }

    public tallerE1Java_DAOClass(
        ArrayList<tallerE1Java_EntityClass> tallere1java_entityclasss    ) {
        this.tallere1java_entityclasss = tallere1java_entityclasss;
    }


    public List<tallerE1Java_EntityClass> getTallere1java_entityclasss() {
        return tallere1java_entityclasss;
    }

    public void addTallere1java_entityclass(Tallere1java_entityclass tallere1java_entityclass) {
        this.tallere1java_entityclasss.add(tallere1java_entityclass);
    }

}