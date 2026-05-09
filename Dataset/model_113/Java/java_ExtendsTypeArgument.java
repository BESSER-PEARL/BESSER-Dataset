





import java.util.List;
import java.util.ArrayList;

public class java_ExtendsTypeArgument extends TypeArgument {






    private List<java_TypeReference> java_typereferences;


    public java_ExtendsTypeArgument(
    ) {
        super(
        );
        this.java_typereferences = new ArrayList<>();
    }

    public java_ExtendsTypeArgument(
        ArrayList<java_TypeReference> java_typereferences    ) {
        this.java_typereferences = java_typereferences;
    }


    public List<java_TypeReference> getJava_typereferences() {
        return java_typereferences;
    }

    public void addJava_typereference(Java_typereference java_typereference) {
        this.java_typereferences.add(java_typereference);
    }

}