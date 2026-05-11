





import java.util.List;
import java.util.ArrayList;

public class tallerE1Java_Program  {






    private List<tallerE1Java_Container> tallere1java_containers;




    private List<tallerE1Java_PrimitiveType> tallere1java_primitivetypes;


    public tallerE1Java_Program(
    ) {
        this.tallere1java_containers = new ArrayList<>();
        this.tallere1java_primitivetypes = new ArrayList<>();
    }

    public tallerE1Java_Program(
        ArrayList<tallerE1Java_Container> tallere1java_containers,        ArrayList<tallerE1Java_PrimitiveType> tallere1java_primitivetypes    ) {
        this.tallere1java_containers = tallere1java_containers;
        this.tallere1java_primitivetypes = tallere1java_primitivetypes;
    }


    public List<tallerE1Java_Container> getTallere1java_containers() {
        return tallere1java_containers;
    }

    public void addTallere1java_container(Tallere1java_container tallere1java_container) {
        this.tallere1java_containers.add(tallere1java_container);
    }
    public List<tallerE1Java_PrimitiveType> getTallere1java_primitivetypes() {
        return tallere1java_primitivetypes;
    }

    public void addTallere1java_primitivetype(Tallere1java_primitivetype tallere1java_primitivetype) {
        this.tallere1java_primitivetypes.add(tallere1java_primitivetype);
    }

}