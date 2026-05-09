





import java.util.List;
import java.util.ArrayList;

public class library_EquipmentGroup extends Base {

    private String description;
    private String count;
    private String name;





    private List<library_Expression> library_expressions;




    private List<library_Parameter> library_parameters;


    public library_EquipmentGroup(
        String description,        String count,        String name    ) {
        super(
        );
        this.description = description;
        this.count = count;
        this.name = name;
        this.library_expressions = new ArrayList<>();
        this.library_parameters = new ArrayList<>();
    }

    public library_EquipmentGroup(
        String description,        String count,        String name        ArrayList<library_Expression> library_expressions,        ArrayList<library_Parameter> library_parameters    ) {
        this.description = description;
        this.count = count;
        this.name = name;
        this.library_expressions = library_expressions;
        this.library_parameters = library_parameters;
    }

    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
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

    public List<library_Expression> getLibrary_expressions() {
        return library_expressions;
    }

    public void addLibrary_expression(Library_expression library_expression) {
        this.library_expressions.add(library_expression);
    }
    public List<library_Parameter> getLibrary_parameters() {
        return library_parameters;
    }

    public void addLibrary_parameter(Library_parameter library_parameter) {
        this.library_parameters.add(library_parameter);
    }

}