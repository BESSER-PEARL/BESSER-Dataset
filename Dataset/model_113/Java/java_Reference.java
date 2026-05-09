





import java.util.List;
import java.util.ArrayList;

public class java_Reference extends PrimaryExpression, TypeArgumentable {






    private java_Reference java_reference;




    private List<java_ArraySelector> java_arrayselectors;


    public java_Reference(
    ) {
        super(
        );
        this.java_arrayselectors = new ArrayList<>();
    }

    public java_Reference(
        ArrayList<java_ArraySelector> java_arrayselectors    ) {
        this.java_arrayselectors = java_arrayselectors;
    }


    public java_Reference getJava_reference() {
        return java_reference;
    }

    public void setJava_reference(java_Reference java_reference) {
        this.java_reference = java_reference;
    }
    public List<java_ArraySelector> getJava_arrayselectors() {
        return java_arrayselectors;
    }

    public void addJava_arrayselector(Java_arrayselector java_arrayselector) {
        this.java_arrayselectors.add(java_arrayselector);
    }

}