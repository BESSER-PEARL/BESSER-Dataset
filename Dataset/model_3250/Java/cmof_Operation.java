





import java.util.List;
import java.util.ArrayList;

public class cmof_Operation extends BehavioralFeature {

    private String upper;
    private String lower;
    private String isUnique;
    private String isQuery;
    private String isOrdered;





    private cmof_DataType cmof_datatype;




    private cmof_DataType cmof_datatype;




    private cmof_Operation cmof_operation;




    private cmof_Class cmof_class;




    private cmof_Class cmof_class;




    private cmof_Parameter cmof_parameter;


    public cmof_Operation(
        String upper,        String lower,        String isUnique,        String isQuery,        String isOrdered    ) {
        super(
        );
        this.upper = upper;
        this.lower = lower;
        this.isUnique = isUnique;
        this.isQuery = isQuery;
        this.isOrdered = isOrdered;
    }


    public String getUpper() {
        return upper;
    }

    public void setUpper(String upper) {
        this.upper = upper;
    }
    public String getLower() {
        return lower;
    }

    public void setLower(String lower) {
        this.lower = lower;
    }
    public String getIsunique() {
        return isUnique;
    }

    public void setIsunique(String isUnique) {
        this.isUnique = isUnique;
    }
    public String getIsquery() {
        return isQuery;
    }

    public void setIsquery(String isQuery) {
        this.isQuery = isQuery;
    }
    public String getIsordered() {
        return isOrdered;
    }

    public void setIsordered(String isOrdered) {
        this.isOrdered = isOrdered;
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
    public cmof_Operation getCmof_operation() {
        return cmof_operation;
    }

    public void setCmof_operation(cmof_Operation cmof_operation) {
        this.cmof_operation = cmof_operation;
    }
    public cmof_Class getCmof_class() {
        return cmof_class;
    }

    public void setCmof_class(cmof_Class cmof_class) {
        this.cmof_class = cmof_class;
    }
    public cmof_Class getCmof_class() {
        return cmof_class;
    }

    public void setCmof_class(cmof_Class cmof_class) {
        this.cmof_class = cmof_class;
    }
    public cmof_Parameter getCmof_parameter() {
        return cmof_parameter;
    }

    public void setCmof_parameter(cmof_Parameter cmof_parameter) {
        this.cmof_parameter = cmof_parameter;
    }

}