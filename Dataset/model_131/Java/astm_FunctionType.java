





import java.util.List;
import java.util.ArrayList;

public class astm_FunctionType extends Type {






    private List<astm_FormalParameterType> astm_formalparametertypes;




    private astm_TypeReference astm_typereference;


    public astm_FunctionType(
    ) {
        super(
        );
        this.astm_formalparametertypes = new ArrayList<>();
    }

    public astm_FunctionType(
        ArrayList<astm_FormalParameterType> astm_formalparametertypes    ) {
        this.astm_formalparametertypes = astm_formalparametertypes;
    }


    public List<astm_FormalParameterType> getAstm_formalparametertypes() {
        return astm_formalparametertypes;
    }

    public void addAstm_formalparametertype(Astm_formalparametertype astm_formalparametertype) {
        this.astm_formalparametertypes.add(astm_formalparametertype);
    }
    public astm_TypeReference getAstm_typereference() {
        return astm_typereference;
    }

    public void setAstm_typereference(astm_TypeReference astm_typereference) {
        this.astm_typereference = astm_typereference;
    }

}