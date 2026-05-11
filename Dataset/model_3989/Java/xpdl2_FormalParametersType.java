





import java.util.List;
import java.util.ArrayList;

public class xpdl2_FormalParametersType  {






    private List<xpdl2_FormalParameterType> xpdl2_formalparametertypes;


    public xpdl2_FormalParametersType(
    ) {
        this.xpdl2_formalparametertypes = new ArrayList<>();
    }

    public xpdl2_FormalParametersType(
        ArrayList<xpdl2_FormalParameterType> xpdl2_formalparametertypes    ) {
        this.xpdl2_formalparametertypes = xpdl2_formalparametertypes;
    }


    public List<xpdl2_FormalParameterType> getXpdl2_formalparametertypes() {
        return xpdl2_formalparametertypes;
    }

    public void addXpdl2_formalparametertype(Xpdl2_formalparametertype xpdl2_formalparametertype) {
        this.xpdl2_formalparametertypes.add(xpdl2_formalparametertype);
    }

}