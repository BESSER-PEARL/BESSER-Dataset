





import java.util.List;
import java.util.ArrayList;

public class JTL_template_ObjectTemplateExp extends TemplateExp {

    private String referredClass;



    public JTL_template_ObjectTemplateExp(
        String referredClass    ) {
        super(
        );
        this.referredClass = referredClass;
    }


    public String getReferredclass() {
        return referredClass;
    }

    public void setReferredclass(String referredClass) {
        this.referredClass = referredClass;
    }


}