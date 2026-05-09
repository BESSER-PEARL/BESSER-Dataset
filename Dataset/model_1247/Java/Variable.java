





import java.util.List;
import java.util.ArrayList;

public class Variable  {






    private mtl_InitSection mtl_initsection;




    private mtl_Query mtl_query;




    private mtl_Macro mtl_macro;




    private mtl_Template mtl_template;


    public Variable(
    ) {
    }



    public mtl_InitSection getMtl_initsection() {
        return mtl_initsection;
    }

    public void setMtl_initsection(mtl_InitSection mtl_initsection) {
        this.mtl_initsection = mtl_initsection;
    }
    public mtl_Query getMtl_query() {
        return mtl_query;
    }

    public void setMtl_query(mtl_Query mtl_query) {
        this.mtl_query = mtl_query;
    }
    public mtl_Macro getMtl_macro() {
        return mtl_macro;
    }

    public void setMtl_macro(mtl_Macro mtl_macro) {
        this.mtl_macro = mtl_macro;
    }
    public mtl_Template getMtl_template() {
        return mtl_template;
    }

    public void setMtl_template(mtl_Template mtl_template) {
        this.mtl_template = mtl_template;
    }

}