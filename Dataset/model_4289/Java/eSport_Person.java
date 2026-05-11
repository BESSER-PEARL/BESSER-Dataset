





import java.util.List;
import java.util.ArrayList;

public class eSport_Person  {

    private int age;
    private String description;
    private String name;





    private List<eSport_Capacity> esport_capacitys;


    public eSport_Person(
        int age,        String description,        String name    ) {
        this.age = age;
        this.description = description;
        this.name = name;
        this.esport_capacitys = new ArrayList<>();
    }

    public eSport_Person(
        int age,        String description,        String name        ArrayList<eSport_Capacity> esport_capacitys    ) {
        this.age = age;
        this.description = description;
        this.name = name;
        this.esport_capacitys = esport_capacitys;
    }

    public int getAge() {
        return age;
    }

    public void setAge(int age) {
        this.age = age;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<eSport_Capacity> getEsport_capacitys() {
        return esport_capacitys;
    }

    public void addEsport_capacity(Esport_capacity esport_capacity) {
        this.esport_capacitys.add(esport_capacity);
    }

}