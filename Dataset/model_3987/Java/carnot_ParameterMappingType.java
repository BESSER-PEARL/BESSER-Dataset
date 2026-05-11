





import java.util.List;
import java.util.ArrayList;

public class carnot_ParameterMappingType extends IModelElement {

    private String parameterPath;
    private String dataPath;
    private String parameter;



    public carnot_ParameterMappingType(
        String parameterPath,        String dataPath,        String parameter    ) {
        super(
        );
        this.parameterPath = parameterPath;
        this.dataPath = dataPath;
        this.parameter = parameter;
    }


    public String getParameterpath() {
        return parameterPath;
    }

    public void setParameterpath(String parameterPath) {
        this.parameterPath = parameterPath;
    }
    public String getDatapath() {
        return dataPath;
    }

    public void setDatapath(String dataPath) {
        this.dataPath = dataPath;
    }
    public String getParameter() {
        return parameter;
    }

    public void setParameter(String parameter) {
        this.parameter = parameter;
    }


}