





import java.util.List;
import java.util.ArrayList;

public class lobj_Author  {

    private String email;
    private String id;
    private String credittype;





    private lobj_Source lobj_source;




    private lobj_ModuleMeta lobj_modulemeta;




    private lobj_Address lobj_address;




    private lobj_LuMeta lobj_lumeta;


    public lobj_Author(
        String email,        String id,        String credittype    ) {
        this.email = email;
        this.id = id;
        this.credittype = credittype;
    }


    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getCredittype() {
        return credittype;
    }

    public void setCredittype(String credittype) {
        this.credittype = credittype;
    }

    public lobj_Source getLobj_source() {
        return lobj_source;
    }

    public void setLobj_source(lobj_Source lobj_source) {
        this.lobj_source = lobj_source;
    }
    public lobj_ModuleMeta getLobj_modulemeta() {
        return lobj_modulemeta;
    }

    public void setLobj_modulemeta(lobj_ModuleMeta lobj_modulemeta) {
        this.lobj_modulemeta = lobj_modulemeta;
    }
    public lobj_Address getLobj_address() {
        return lobj_address;
    }

    public void setLobj_address(lobj_Address lobj_address) {
        this.lobj_address = lobj_address;
    }
    public lobj_LuMeta getLobj_lumeta() {
        return lobj_lumeta;
    }

    public void setLobj_lumeta(lobj_LuMeta lobj_lumeta) {
        this.lobj_lumeta = lobj_lumeta;
    }

}