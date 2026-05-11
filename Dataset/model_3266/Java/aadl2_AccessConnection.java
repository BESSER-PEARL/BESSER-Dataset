





import java.util.List;
import java.util.ArrayList;

public class aadl2_AccessConnection extends Connection {

    private String accessCategory;





    private aadl2_ComponentImplementation aadl2_componentimplementation;


    public aadl2_AccessConnection(
        String accessCategory    ) {
        super(
        );
        this.accessCategory = accessCategory;
    }


    public String getAccesscategory() {
        return accessCategory;
    }

    public void setAccesscategory(String accessCategory) {
        this.accessCategory = accessCategory;
    }

    public aadl2_ComponentImplementation getAadl2_componentimplementation() {
        return aadl2_componentimplementation;
    }

    public void setAadl2_componentimplementation(aadl2_ComponentImplementation aadl2_componentimplementation) {
        this.aadl2_componentimplementation = aadl2_componentimplementation;
    }

}