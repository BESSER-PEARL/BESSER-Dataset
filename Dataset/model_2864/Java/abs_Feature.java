





import java.util.List;
import java.util.ArrayList;

public class abs_Feature  {

    private String p;
    private String attr_assignment;





    private abs_Productline_decl abs_productline_decl;




    private abs_Feature_decl abs_feature_decl;




    private abs_Product_decl abs_product_decl;


    public abs_Feature(
        String p,        String attr_assignment    ) {
        this.p = p;
        this.attr_assignment = attr_assignment;
    }


    public String getP() {
        return p;
    }

    public void setP(String p) {
        this.p = p;
    }
    public String getAttr_assignment() {
        return attr_assignment;
    }

    public void setAttr_assignment(String attr_assignment) {
        this.attr_assignment = attr_assignment;
    }

    public abs_Productline_decl getAbs_productline_decl() {
        return abs_productline_decl;
    }

    public void setAbs_productline_decl(abs_Productline_decl abs_productline_decl) {
        this.abs_productline_decl = abs_productline_decl;
    }
    public abs_Feature_decl getAbs_feature_decl() {
        return abs_feature_decl;
    }

    public void setAbs_feature_decl(abs_Feature_decl abs_feature_decl) {
        this.abs_feature_decl = abs_feature_decl;
    }
    public abs_Product_decl getAbs_product_decl() {
        return abs_product_decl;
    }

    public void setAbs_product_decl(abs_Product_decl abs_product_decl) {
        this.abs_product_decl = abs_product_decl;
    }

}