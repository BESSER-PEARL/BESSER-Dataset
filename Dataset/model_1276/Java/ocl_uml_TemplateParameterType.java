





import java.util.List;
import java.util.ArrayList;

public class ocl_uml_TemplateParameterType  {






    private List<uml_ocl_Operation> uml_ocl_operations;


    public ocl_uml_TemplateParameterType(
    ) {
        this.uml_ocl_operations = new ArrayList<>();
    }

    public ocl_uml_TemplateParameterType(
        ArrayList<uml_ocl_Operation> uml_ocl_operations    ) {
        this.uml_ocl_operations = uml_ocl_operations;
    }


    public List<uml_ocl_Operation> getUml_ocl_operations() {
        return uml_ocl_operations;
    }

    public void addUml_ocl_operation(Uml_ocl_operation uml_ocl_operation) {
        this.uml_ocl_operations.add(uml_ocl_operation);
    }

}