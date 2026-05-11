





import java.util.List;
import java.util.ArrayList;

public class abs_Product_expr  {






    private abs_Product_decl abs_product_decl;




    private abs_Product_expr abs_product_expr;




    private List<abs_Feature_decl> abs_feature_decls;




    private abs_Product_decl abs_product_decl;




    private abs_Product_expr abs_product_expr;


    public abs_Product_expr(
    ) {
        this.abs_feature_decls = new ArrayList<>();
    }

    public abs_Product_expr(
        ArrayList<abs_Feature_decl> abs_feature_decls    ) {
        this.abs_feature_decls = abs_feature_decls;
    }


    public abs_Product_decl getAbs_product_decl() {
        return abs_product_decl;
    }

    public void setAbs_product_decl(abs_Product_decl abs_product_decl) {
        this.abs_product_decl = abs_product_decl;
    }
    public abs_Product_expr getAbs_product_expr() {
        return abs_product_expr;
    }

    public void setAbs_product_expr(abs_Product_expr abs_product_expr) {
        this.abs_product_expr = abs_product_expr;
    }
    public List<abs_Feature_decl> getAbs_feature_decls() {
        return abs_feature_decls;
    }

    public void addAbs_feature_decl(Abs_feature_decl abs_feature_decl) {
        this.abs_feature_decls.add(abs_feature_decl);
    }
    public abs_Product_decl getAbs_product_decl() {
        return abs_product_decl;
    }

    public void setAbs_product_decl(abs_Product_decl abs_product_decl) {
        this.abs_product_decl = abs_product_decl;
    }
    public abs_Product_expr getAbs_product_expr() {
        return abs_product_expr;
    }

    public void setAbs_product_expr(abs_Product_expr abs_product_expr) {
        this.abs_product_expr = abs_product_expr;
    }

}