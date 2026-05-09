





import java.util.List;
import java.util.ArrayList;

public class java_TypeParameter extends Classifier {






    private List<java_TypeReference> java_typereferences;




    private java_TypeParametrizable java_typeparametrizable;


    public java_TypeParameter(
    ) {
        super(
        );
        this.java_typereferences = new ArrayList<>();
    }

    public java_TypeParameter(
        ArrayList<java_TypeReference> java_typereferences    ) {
        this.java_typereferences = java_typereferences;
    }


    public List<java_TypeReference> getJava_typereferences() {
        return java_typereferences;
    }

    public void addJava_typereference(Java_typereference java_typereference) {
        this.java_typereferences.add(java_typereference);
    }
    public java_TypeParametrizable getJava_typeparametrizable() {
        return java_typeparametrizable;
    }

    public void setJava_typeparametrizable(java_TypeParametrizable java_typeparametrizable) {
        this.java_typeparametrizable = java_typeparametrizable;
    }

}