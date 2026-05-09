





import java.util.List;
import java.util.ArrayList;

public class pivot_Feature extends TypedMultiplicityElement {

    private String implementation;
    private String implementationClass;



    public pivot_Feature(
        String implementation,        String implementationClass    ) {
        super(
        );
        this.implementation = implementation;
        this.implementationClass = implementationClass;
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