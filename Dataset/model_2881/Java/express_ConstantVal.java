





import java.util.List;
import java.util.ArrayList;

public class express_ConstantVal  {

    private String name;





    private express_DataType express_datatype;




    private express_Rule express_rule;


    public express_ConstantVal(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public express_DataType getExpress_datatype() {
        return express_datatype;
    }

    public void setExpress_datatype(express_DataType express_datatype) {
        this.express_datatype = express_datatype;
    }
    public express_Rule getExpress_rule() {
        return express_rule;
    }

    public void setExpress_rule(express_Rule express_rule) {
        this.express_rule = express_rule;
    }

}