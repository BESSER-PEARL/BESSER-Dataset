





import java.util.List;
import java.util.ArrayList;

public class pivot_Feature extends TypedElement {

    private String isStatic;
    private String implementation;
    private String implementationClass;



    public pivot_Feature(
        String isStatic,        String implementation,        String implementationClass    ) {
        super(
        );
        this.isStatic = isStatic;
        this.implementation = implementation;
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
    public String getImplementationclass() {
        return implementationClass;
    }

    public void setImplementationclass(String implementationClass) {
        this.implementationClass = implementationClass;
    }


}