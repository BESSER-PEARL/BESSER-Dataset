





import java.util.List;
import java.util.ArrayList;

public class library_EquipmentGroup extends Base {

    private String count;
    private String name;
    private String description;





    private List<library_Expression> library_expressions;


    public library_EquipmentGroup(
        String count,        String name,        String description    ) {
        super(
        );
        this.count = count;
        this.name = name;
        this.description = description;
        this.library_expressions = new ArrayList<>();
    }

    public library_EquipmentGroup(
        String count,        String name,        String description        ArrayList<library_Expression> library_expressions    ) {
        this.count = count;
        this.name = name;
        this.description = description;
        this.library_expressions = library_expressions;
    }

    public String getCount() {
        return count;
    }

    public void setCount(String count) {
        this.count = count;
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

    public List<library_Expression> getLibrary_expressions() {
        return library_expressions;
    }

    public void addLibrary_expression(Library_expression library_expression) {
        this.library_expressions.add(library_expression);
    }

}