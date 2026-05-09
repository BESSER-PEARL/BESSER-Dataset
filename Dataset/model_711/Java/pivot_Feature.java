





import java.util.List;
import java.util.ArrayList;

public class pivot_Feature extends TypedMultiplicityElement {

    private String implementationClass;
    private String implementation;



    public pivot_Feature(
        String implementationClass,        String implementation    ) {
        super(
        );
        this.implementationClass = implementationClass;
        this.implementation = implementation;
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


}