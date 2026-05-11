





import java.util.List;
import java.util.ArrayList;

public class model_ss_XtendMember extends XtendAnnotationTarget {

    private String modifiers;





    private XtendTypeDeclaration xtendtypedeclaration;


    public model_ss_XtendMember(
        String modifiers    ) {
        super(
        );
        this.modifiers = modifiers;
    }


    public String getModifiers() {
        return modifiers;
    }

    public void setModifiers(String modifiers) {
        this.modifiers = modifiers;
    }

    public XtendTypeDeclaration getXtendtypedeclaration() {
        return xtendtypedeclaration;
    }

    public void setXtendtypedeclaration(XtendTypeDeclaration xtendtypedeclaration) {
        this.xtendtypedeclaration = xtendtypedeclaration;
    }

}