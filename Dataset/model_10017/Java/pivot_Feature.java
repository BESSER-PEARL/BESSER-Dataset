





import java.util.List;
import java.util.ArrayList;

public class pivot_Feature extends TypedElement {

    private String implementationClass;
    private String implementation;
    private String isStatic;



    public pivot_Feature(
        String implementationClass,        String implementation,        String isStatic    ) {
        super(
        );
        this.implementationClass = implementationClass;
        this.implementation = implementation;
        this.isStatic = isStatic;
    }


    public String getImplementationclass() {
        return implementationClass;
    }

    public void setImplementationclass(String implementationClass) {
        this.implementationClass = implementationClass;
    }
    public String getImplementation() {
        return implementation;
    }

    public void setImplementation(String implementation) {
        this.implementation = implementation;
    }
    public String getIsstatic() {
        return isStatic;
    }

    public void setIsstatic(String isStatic) {
        this.isStatic = isStatic;
    }


}