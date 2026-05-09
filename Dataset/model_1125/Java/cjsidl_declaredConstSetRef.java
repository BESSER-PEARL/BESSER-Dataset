





import java.util.List;
import java.util.ArrayList;

public class cjsidl_declaredConstSetRef  {

    private String name;
    private String comment;





    private cjsidl_declaredTypeSet cjsidl_declaredtypeset;




    private cjsidl_declaredConstSet cjsidl_declaredconstset;




    private cjsidl_declaredConstSet cjsidl_declaredconstset;


    public cjsidl_declaredConstSetRef(
        String name,        String comment    ) {
        this.name = name;
        this.comment = comment;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getComment() {
        return comment;
    }

    public void setComment(String comment) {
        this.comment = comment;
    }

    public cjsidl_declaredTypeSet getCjsidl_declaredtypeset() {
        return cjsidl_declaredtypeset;
    }

    public void setCjsidl_declaredtypeset(cjsidl_declaredTypeSet cjsidl_declaredtypeset) {
        this.cjsidl_declaredtypeset = cjsidl_declaredtypeset;
    }
    public cjsidl_declaredConstSet getCjsidl_declaredconstset() {
        return cjsidl_declaredconstset;
    }

    public void setCjsidl_declaredconstset(cjsidl_declaredConstSet cjsidl_declaredconstset) {
        this.cjsidl_declaredconstset = cjsidl_declaredconstset;
    }
    public cjsidl_declaredConstSet getCjsidl_declaredconstset() {
        return cjsidl_declaredconstset;
    }

    public void setCjsidl_declaredconstset(cjsidl_declaredConstSet cjsidl_declaredconstset) {
        this.cjsidl_declaredconstset = cjsidl_declaredconstset;
    }

}