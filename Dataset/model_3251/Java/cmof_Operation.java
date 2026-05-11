





import java.util.List;
import java.util.ArrayList;

public class cmof_Operation extends BehavioralFeature {

    private String isOrdered;
    private String isQuery;
    private String upper;
    private String isUnique;
    private String lower;





    private cmof_Class cmof_class;




    private cmof_DataType cmof_datatype;




    private cmof_DataType cmof_datatype;




    private List<cmof_Operation> cmof_operations;




    private cmof_Parameter cmof_parameter;




    private cmof_Class cmof_class;


    public cmof_Operation(
        String isOrdered,        String isQuery,        String upper,        String isUnique,        String lower    ) {
        super(
        );
        this.isOrdered = isOrdered;
        this.isQuery = isQuery;
        this.upper = upper;
        this.isUnique = isUnique;
        this.lower = lower;
        this.cmof_operations = new ArrayList<>();
    }

    public cmof_Operation(
        String isOrdered,        String isQuery,        String upper,        String isUnique,        String lower        ArrayList<cmof_Operation> cmof_operations    ) {
        this.isOrdered = isOrdered;
        this.isQuery = isQuery;
        this.upper = upper;
        this.isUnique = isUnique;
        this.lower = lower;
        this.cmof_operations = cmof_operations;
    }

    public String getIsordered() {
        return isOrdered;
    }

    public void setIsordered(String isOrdered) {
        this.isOrdered = isOrdered;
    }
    public String getIsquery() {
        return isQuery;
    }

    public void setIsquery(String isQuery) {
        this.isQuery = isQuery;
    }
    public String getUpper() {
        return upper;
    }

    public void setUpper(String upper) {
        this.upper = upper;
    }
    public String getIsunique() {
        return isUnique;
    }

    public void setIsunique(String isUnique) {
        this.isUnique = isUnique;
    }
    public String getLower() {
        return lower;
    }

    public void setLower(String lower) {
        this.lower = lower;
    }

    public cmof_Class getCmof_class() {
        return cmof_class;
    }

    public void setCmof_class(cmof_Class cmof_class) {
        this.cmof_class = cmof_class;
    }
    public cmof_DataType getCmof_datatype() {
        return cmof_datatype;
    }

    public void setCmof_datatype(cmof_DataType cmof_datatype) {
        this.cmof_datatype = cmof_datatype;
    }
    public cmof_DataType getCmof_datatype() {
        return cmof_datatype;
    }

    public void setCmof_datatype(cmof_DataType cmof_datatype) {
        this.cmof_datatype = cmof_datatype;
    }
    public List<cmof_Operation> getCmof_operations() {
        return cmof_operations;
    }

    public void addCmof_operation(Cmof_operation cmof_operation) {
        this.cmof_operations.add(cmof_operation);
    }
    public cmof_Parameter getCmof_parameter() {
        return cmof_parameter;
    }

    public void setCmof_parameter(cmof_Parameter cmof_parameter) {
        this.cmof_parameter = cmof_parameter;
    }
    public cmof_Class getCmof_class() {
        return cmof_class;
    }

    public void setCmof_class(cmof_Class cmof_class) {
        this.cmof_class = cmof_class;
    }

}