





import java.util.List;
import java.util.ArrayList;

public class pivot_Feature extends TypedElement {

    private String implementationClass;
    private String isStatic;
    private String implementation;



    public pivot_Feature(
        String implementationClass,        String isStatic,        String implementation    ) {
        super(
        );
        this.implementationClass = implementationClass;
        this.isStatic = isStatic;
        this.implementation = implementation;
    }


    public String getImplementationclass() {
        return implementationClass;
    }

    public void setImplementationclass(String implementationClass) {
        this.implementationClass = implementationClass;
    }
    public String getIsstatic() {
        return isStatic;
    }

    public void setIsstatic(String isStatic) {
        this.isStatic = isStatic;
    }
    public String getImplementation() {
        return implementation;
    }

    public void setImplementation(String implementation) {
        this.implementation = implementation;
    }


}