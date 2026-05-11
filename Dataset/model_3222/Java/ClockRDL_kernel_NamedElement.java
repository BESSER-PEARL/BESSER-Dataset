





import java.util.List;
import java.util.ArrayList;

public class ClockRDL_kernel_NamedElement extends Element {

    private String name;



    public ClockRDL_kernel_NamedElement(
        String name    ) {
        super(
        );
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}