





import java.util.List;
import java.util.ArrayList;

public class mtl_TemplateInvocation extends TemplateExpression {

    private boolean super;





    private mtl_Template mtl_template;


    public mtl_TemplateInvocation(
        boolean super    ) {
        super(
        );
        this.super = super;
    }


    public boolean getSuper() {
        return super;
    }

    public void setSuper(boolean super) {
        this.super = super;
    }

    public mtl_Template getMtl_template() {
        return mtl_template;
    }

    public void setMtl_template(mtl_Template mtl_template) {
        this.mtl_template = mtl_template;
    }

}