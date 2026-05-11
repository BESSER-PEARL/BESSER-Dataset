





import java.util.List;
import java.util.ArrayList;

public class express_FormalParam  {

    private String paramName;





    private express_DataType express_datatype;




    private express_ParameterList express_parameterlist;


    public express_FormalParam(
        String paramName    ) {
        this.paramName = paramName;
    }


    public String getParamname() {
        return paramName;
    }

    public void setParamname(String paramName) {
        this.paramName = paramName;
    }

    public express_DataType getExpress_datatype() {
        return express_datatype;
    }

    public void setExpress_datatype(express_DataType express_datatype) {
        this.express_datatype = express_datatype;
    }
    public express_ParameterList getExpress_parameterlist() {
        return express_parameterlist;
    }

    public void setExpress_parameterlist(express_ParameterList express_parameterlist) {
        this.express_parameterlist = express_parameterlist;
    }

}