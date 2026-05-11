





import java.util.List;
import java.util.ArrayList;

public class relational_Domain extends DistinctUserDefinedType {

    private String defaultValue;
    private boolean nullable;





    private relational_CheckConstraint relational_checkconstraint;




    private relational_DataType relational_datatype;


    public relational_Domain(
        String defaultValue,        boolean nullable    ) {
        super(
        );
        this.defaultValue = defaultValue;
        this.nullable = nullable;
    }


    public String getDefaultvalue() {
        return defaultValue;
    }

    public void setDefaultvalue(String defaultValue) {
        this.defaultValue = defaultValue;
    }
    public boolean getNullable() {
        return nullable;
    }

    public void setNullable(boolean nullable) {
        this.nullable = nullable;
    }

    public relational_CheckConstraint getRelational_checkconstraint() {
        return relational_checkconstraint;
    }

    public void setRelational_checkconstraint(relational_CheckConstraint relational_checkconstraint) {
        this.relational_checkconstraint = relational_checkconstraint;
    }
    public relational_DataType getRelational_datatype() {
        return relational_datatype;
    }

    public void setRelational_datatype(relational_DataType relational_datatype) {
        this.relational_datatype = relational_datatype;
    }

}