





import java.util.List;
import java.util.ArrayList;

public class gast_accesses_InheritanceTypeAccess extends TypeAccess {

    private boolean implementationInheritance;



    public gast_accesses_InheritanceTypeAccess(
        boolean implementationInheritance    ) {
        super(
        );
        this.implementationInheritance = implementationInheritance;
    }


    public boolean getImplementationinheritance() {
        return implementationInheritance;
    }

    public void setImplementationinheritance(boolean implementationInheritance) {
        this.implementationInheritance = implementationInheritance;
    }


}