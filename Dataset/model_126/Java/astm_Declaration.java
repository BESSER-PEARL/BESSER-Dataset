





import java.util.List;
import java.util.ArrayList;

public class astm_Declaration extends DeclarationOrDefinition {






    private astm_TypeReference astm_typereference;




    private astm_Name astm_name;




    private astm_Definition astm_definition;


    public astm_Declaration(
    ) {
        super(
        );
    }



    public astm_TypeReference getAstm_typereference() {
        return astm_typereference;
    }

    public void setAstm_typereference(astm_TypeReference astm_typereference) {
        this.astm_typereference = astm_typereference;
    }
    public astm_Name getAstm_name() {
        return astm_name;
    }

    public void setAstm_name(astm_Name astm_name) {
        this.astm_name = astm_name;
    }
    public astm_Definition getAstm_definition() {
        return astm_definition;
    }

    public void setAstm_definition(astm_Definition astm_definition) {
        this.astm_definition = astm_definition;
    }

}