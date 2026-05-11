





import java.util.List;
import java.util.ArrayList;

public class express_LocalVar  {

    private String varname;





    private express_Rule express_rule;




    private express_DataType express_datatype;




    private express_Function express_function;


    public express_LocalVar(
        String varname    ) {
        this.varname = varname;
    }


    public String getVarname() {
        return varname;
    }

    public void setVarname(String varname) {
        this.varname = varname;
    }

    public express_Rule getExpress_rule() {
        return express_rule;
    }

    public void setExpress_rule(express_Rule express_rule) {
        this.express_rule = express_rule;
    }
    public express_DataType getExpress_datatype() {
        return express_datatype;
    }

    public void setExpress_datatype(express_DataType express_datatype) {
        this.express_datatype = express_datatype;
    }
    public express_Function getExpress_function() {
        return express_function;
    }

    public void setExpress_function(express_Function express_function) {
        this.express_function = express_function;
    }

}