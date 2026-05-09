





import java.util.List;
import java.util.ArrayList;

public class ocl_cst_CallExpCS extends OCLExpressionCS {

    private String accessor;



    public ocl_cst_CallExpCS(
        String accessor    ) {
        super(
        );
        this.accessor = accessor;
    }


    public String getAccessor() {
        return accessor;
    }

    public void setAccessor(String accessor) {
        this.accessor = accessor;
    }


}