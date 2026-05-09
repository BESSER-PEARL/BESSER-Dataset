





import java.util.List;
import java.util.ArrayList;

public class atl_n_ocl_OCL_Operation extends OclFeature {

    private String name;





    private OclType ocltype;




    private OclExpression oclexpression;




    private List<Parameter> parameters;


    public atl_n_ocl_OCL_Operation(
        String name    ) {
        super(
        );
        this.name = name;
        this.parameters = new ArrayList<>();
    }

    public atl_n_ocl_OCL_Operation(
        String name        ArrayList<Parameter> parameters    ) {
        this.name = name;
        this.parameters = parameters;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public OclType getOcltype() {
        return ocltype;
    }

    public void setOcltype(OclType ocltype) {
        this.ocltype = ocltype;
    }
    public OclExpression getOclexpression() {
        return oclexpression;
    }

    public void setOclexpression(OclExpression oclexpression) {
        this.oclexpression = oclexpression;
    }
    public List<Parameter> getParameters() {
        return parameters;
    }

    public void addParameter(Parameter parameter) {
        this.parameters.add(parameter);
    }

}