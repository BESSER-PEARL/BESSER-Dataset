





import java.util.List;
import java.util.ArrayList;

public class cjsidl_constDef  {

    private String comment;
    private String constValue;
    private String name;
    private String fieldUnits;





    private cjsidl_declaredConstSet cjsidl_declaredconstset;


    public cjsidl_constDef(
        String comment,        String constValue,        String name,        String fieldUnits    ) {
        this.comment = comment;
        this.constValue = constValue;
        this.name = name;
        this.fieldUnits = fieldUnits;
    }


    public String getComment() {
        return comment;
    }

    public void setComment(String comment) {
        this.comment = comment;
    }
    public String getConstvalue() {
        return constValue;
    }

    public void setConstvalue(String constValue) {
        this.constValue = constValue;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getFieldunits() {
        return fieldUnits;
    }

    public void setFieldunits(String fieldUnits) {
        this.fieldUnits = fieldUnits;
    }

    public cjsidl_declaredConstSet getCjsidl_declaredconstset() {
        return cjsidl_declaredconstset;
    }

    public void setCjsidl_declaredconstset(cjsidl_declaredConstSet cjsidl_declaredconstset) {
        this.cjsidl_declaredconstset = cjsidl_declaredconstset;
    }

}