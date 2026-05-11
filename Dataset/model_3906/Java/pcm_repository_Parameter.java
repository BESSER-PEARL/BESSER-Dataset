





import java.util.List;
import java.util.ArrayList;

public class pcm_repository_Parameter  {

    private String modifier__Parameter;
    private String parameterName;





    private DataType datatype;


    public pcm_repository_Parameter(
        String modifier__Parameter,        String parameterName    ) {
        this.modifier__Parameter = modifier__Parameter;
        this.parameterName = parameterName;
    }


    public String getModifier__parameter() {
        return modifier__Parameter;
    }

    public void setModifier__parameter(String modifier__Parameter) {
        this.modifier__Parameter = modifier__Parameter;
    }
    public String getParametername() {
        return parameterName;
    }

    public void setParametername(String parameterName) {
        this.parameterName = parameterName;
    }

    public DataType getDatatype() {
        return datatype;
    }

    public void setDatatype(DataType datatype) {
        this.datatype = datatype;
    }

}