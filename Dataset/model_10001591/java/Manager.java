





import java.util.List;
import java.util.ArrayList;

public class Manager  {

    private String name;
    private int id;





    private List<Receptionist> receptionists;


    public Manager(
        String name,        int id    ) {
        this.name = name;
        this.id = id;
        this.receptionists = new ArrayList<>();
    }

    public Manager(
        String name,        int id        ArrayList<Receptionist> receptionists    ) {
        this.name = name;
        this.id = id;
        this.receptionists = receptionists;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public List<Receptionist> getReceptionists() {
        return receptionists;
    }

    public void addReceptionist(Receptionist receptionist) {
        this.receptionists.add(receptionist);
    }

}