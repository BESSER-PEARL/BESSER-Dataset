





import java.util.List;
import java.util.ArrayList;

public class JDTAST_Annotation extends ExtendedModifier, Expression {






    private JDTAST_Name jdtast_name;




    private JDTAST_PackageDeclaration jdtast_packagedeclaration;


    public JDTAST_Annotation(
    ) {
        super(
        );
    }



    public JDTAST_Name getJdtast_name() {
        return jdtast_name;
    }

    public void setJdtast_name(JDTAST_Name jdtast_name) {
        this.jdtast_name = jdtast_name;
    }
    public JDTAST_PackageDeclaration getJdtast_packagedeclaration() {
        return jdtast_packagedeclaration;
    }

    public void setJdtast_packagedeclaration(JDTAST_PackageDeclaration jdtast_packagedeclaration) {
        this.jdtast_packagedeclaration = jdtast_packagedeclaration;
    }

}