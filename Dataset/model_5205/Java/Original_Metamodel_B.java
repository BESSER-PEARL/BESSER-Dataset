





import java.util.List;
import java.util.ArrayList;

public class Original_Metamodel_B  {

    private String propertyB;





    private Original_Metamodel_A original_metamodel_a;


    public Original_Metamodel_B(
        String propertyB    ) {
        this.propertyB = propertyB;
    }


    public String getPropertyb() {
        return propertyB;
    }

    public void setPropertyb(String propertyB) {
        this.propertyB = propertyB;
    }

    public Original_Metamodel_A getOriginal_metamodel_a() {
        return original_metamodel_a;
    }

    public void setOriginal_metamodel_a(Original_Metamodel_A original_metamodel_a) {
        this.original_metamodel_a = original_metamodel_a;
    }

}