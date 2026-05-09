





import java.util.List;
import java.util.ArrayList;

public class gastm_Declaration extends DeclarationOrDefinition {






    private gastm_TypeReference gastm_typereference;




    private gastm_Definition gastm_definition;




    private gastm_Name gastm_name;


    public gastm_Declaration(
    ) {
        super(
        );
    }



    public gastm_TypeReference getGastm_typereference() {
        return gastm_typereference;
    }

    public void setGastm_typereference(gastm_TypeReference gastm_typereference) {
        this.gastm_typereference = gastm_typereference;
    }
    public gastm_Definition getGastm_definition() {
        return gastm_definition;
    }

    public void setGastm_definition(gastm_Definition gastm_definition) {
        this.gastm_definition = gastm_definition;
    }
    public gastm_Name getGastm_name() {
        return gastm_name;
    }

    public void setGastm_name(gastm_Name gastm_name) {
        this.gastm_name = gastm_name;
    }

}