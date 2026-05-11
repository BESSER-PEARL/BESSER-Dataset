





import java.util.List;
import java.util.ArrayList;

public class classes_Operation extends BehavioralFeature {

    private boolean unique;
    private String lower;
    private boolean query;
    private boolean ordered;
    private String upper;





    private classes_Class classes_class;




    private classes_Class classes_class;




    private classes_Type classes_type;




    private List<classes_Operation> classes_operations;


    public classes_Operation(
        boolean unique,        String lower,        boolean query,        boolean ordered,        String upper    ) {
        super(
        );
        this.unique = unique;
        this.lower = lower;
        this.query = query;
        this.ordered = ordered;
        this.upper = upper;
        this.classes_operations = new ArrayList<>();
    }

    public classes_Operation(
        boolean unique,        String lower,        boolean query,        boolean ordered,        String upper        ArrayList<classes_Operation> classes_operations    ) {
        this.unique = unique;
        this.lower = lower;
        this.query = query;
        this.ordered = ordered;
        this.upper = upper;
        this.classes_operations = classes_operations;
    }

    public boolean getUnique() {
        return unique;
    }

    public void setUnique(boolean unique) {
        this.unique = unique;
    }
    public String getLower() {
        return lower;
    }

    public void setLower(String lower) {
        this.lower = lower;
    }
    public boolean getQuery() {
        return query;
    }

    public void setQuery(boolean query) {
        this.query = query;
    }
    public boolean getOrdered() {
        return ordered;
    }

    public void setOrdered(boolean ordered) {
        this.ordered = ordered;
    }
    public String getUpper() {
        return upper;
    }

    public void setUpper(String upper) {
        this.upper = upper;
    }

    public classes_Class getClasses_class() {
        return classes_class;
    }

    public void setClasses_class(classes_Class classes_class) {
        this.classes_class = classes_class;
    }
    public classes_Class getClasses_class() {
        return classes_class;
    }

    public void setClasses_class(classes_Class classes_class) {
        this.classes_class = classes_class;
    }
    public classes_Type getClasses_type() {
        return classes_type;
    }

    public void setClasses_type(classes_Type classes_type) {
        this.classes_type = classes_type;
    }
    public List<classes_Operation> getClasses_operations() {
        return classes_operations;
    }

    public void addClasses_operation(Classes_operation classes_operation) {
        this.classes_operations.add(classes_operation);
    }

}