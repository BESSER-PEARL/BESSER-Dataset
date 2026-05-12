





import java.util.List;
import java.util.ArrayList;

public class Product  {

    private String name;
    private String description;





    private List<Classes> classess;


    public Product(
        String name,        String description    ) {
        this.name = name;
        this.description = description;
        this.classess = new ArrayList<>();
    }

    public Product(
        String name,        String description        ArrayList<Classes> classess    ) {
        this.name = name;
        this.description = description;
        this.classess = classess;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }

    public List<Classes> getClassess() {
        return classess;
    }

    public void addClasses(Classes classes) {
        this.classess.add(classes);
    }

}