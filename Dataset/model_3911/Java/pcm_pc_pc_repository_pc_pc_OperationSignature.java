





import java.util.List;
import java.util.ArrayList;

public class pcm_pc_pc_repository_pc_pc_OperationSignature extends Signature {






    private DataType datatype;




    private List<Parameter> parameters;


    public pcm_pc_pc_repository_pc_pc_OperationSignature(
    ) {
        super(
        );
        this.parameters = new ArrayList<>();
    }

    public pcm_pc_pc_repository_pc_pc_OperationSignature(
        ArrayList<Parameter> parameters    ) {
        this.parameters = parameters;
    }


    public DataType getDatatype() {
        return datatype;
    }

    public void setDatatype(DataType datatype) {
        this.datatype = datatype;
    }
    public List<Parameter> getParameters() {
        return parameters;
    }

    public void addParameter(Parameter parameter) {
        this.parameters.add(parameter);
    }

}