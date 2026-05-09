





import java.util.List;
import java.util.ArrayList;

public class classes_OperationCallExp extends CallExp {






    private classes_Operation classes_operation;




    private List<classes_Argument> classes_arguments;


    public classes_OperationCallExp(
    ) {
        super(
        );
        this.classes_arguments = new ArrayList<>();
    }

    public classes_OperationCallExp(
        ArrayList<classes_Argument> classes_arguments    ) {
        this.classes_arguments = classes_arguments;
    }


    public classes_Operation getClasses_operation() {
        return classes_operation;
    }

    public void setClasses_operation(classes_Operation classes_operation) {
        this.classes_operation = classes_operation;
    }
    public List<classes_Argument> getClasses_arguments() {
        return classes_arguments;
    }

    public void addClasses_argument(Classes_argument classes_argument) {
        this.classes_arguments.add(classes_argument);
    }

}