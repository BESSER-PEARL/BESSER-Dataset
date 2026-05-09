





import java.util.List;
import java.util.ArrayList;

public class java_ArrayInitializer extends ArrayInitializationValue, AnnotationValue {






    private List<java_ArrayInitializationValue> java_arrayinitializationvalues;


    public java_ArrayInitializer(
    ) {
        super(
        );
        this.java_arrayinitializationvalues = new ArrayList<>();
    }

    public java_ArrayInitializer(
        ArrayList<java_ArrayInitializationValue> java_arrayinitializationvalues    ) {
        this.java_arrayinitializationvalues = java_arrayinitializationvalues;
    }


    public List<java_ArrayInitializationValue> getJava_arrayinitializationvalues() {
        return java_arrayinitializationvalues;
    }

    public void addJava_arrayinitializationvalue(Java_arrayinitializationvalue java_arrayinitializationvalue) {
        this.java_arrayinitializationvalues.add(java_arrayinitializationvalue);
    }

}