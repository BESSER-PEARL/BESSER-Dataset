





import java.util.List;
import java.util.ArrayList;

public class ir_ocl_PropertyCallExp extends CallExp {

    private String name;



    public ir_ocl_PropertyCallExp(
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