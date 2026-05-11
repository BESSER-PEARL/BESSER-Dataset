





import java.util.List;
import java.util.ArrayList;

public class express_Function  {

    private String name;





    private express_Schema express_schema;




    private express_DataType express_datatype;




    private List<express_ConstantVal> express_constantvals;


    public express_Function(
        String name    ) {
        this.name = name;
        this.express_constantvals = new ArrayList<>();
    }

    public express_Function(
        String name        ArrayList<express_ConstantVal> express_constantvals    ) {
        this.name = name;
        this.express_constantvals = express_constantvals;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public express_Schema getExpress_schema() {
        return express_schema;
    }

    public void setExpress_schema(express_Schema express_schema) {
        this.express_schema = express_schema;
    }
    public express_DataType getExpress_datatype() {
        return express_datatype;
    }

    public void setExpress_datatype(express_DataType express_datatype) {
        this.express_datatype = express_datatype;
    }
    public List<express_ConstantVal> getExpress_constantvals() {
        return express_constantvals;
    }

    public void addExpress_constantval(Express_constantval express_constantval) {
        this.express_constantvals.add(express_constantval);
    }

}