





import java.util.List;
import java.util.ArrayList;

public class abs_Feature_decl_attribute  {

    private String uBoundary_int;
    private String boundary_val;
    private String lBoundary_int;





    private abs_Feature_decl abs_feature_decl;




    private abs_Fextension abs_fextension;


    public abs_Feature_decl_attribute(
        String uBoundary_int,        String boundary_val,        String lBoundary_int    ) {
        this.uBoundary_int = uBoundary_int;
        this.boundary_val = boundary_val;
        this.lBoundary_int = lBoundary_int;
    }


    public String getUboundary_int() {
        return uBoundary_int;
    }

    public void setUboundary_int(String uBoundary_int) {
        this.uBoundary_int = uBoundary_int;
    }
    public String getBoundary_val() {
        return boundary_val;
    }

    public void setBoundary_val(String boundary_val) {
        this.boundary_val = boundary_val;
    }
    public String getLboundary_int() {
        return lBoundary_int;
    }

    public void setLboundary_int(String lBoundary_int) {
        this.lBoundary_int = lBoundary_int;
    }

    public abs_Feature_decl getAbs_feature_decl() {
        return abs_feature_decl;
    }

    public void setAbs_feature_decl(abs_Feature_decl abs_feature_decl) {
        this.abs_feature_decl = abs_feature_decl;
    }
    public abs_Fextension getAbs_fextension() {
        return abs_fextension;
    }

    public void setAbs_fextension(abs_Fextension abs_fextension) {
        this.abs_fextension = abs_fextension;
    }

}