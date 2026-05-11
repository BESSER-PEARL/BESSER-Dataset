





import java.util.List;
import java.util.ArrayList;

public class ram_Parameter extends TypedElement {






    private ram_Type ram_type;




    private ram_Operation ram_operation;


    public ram_Parameter(
    ) {
        super(
        );
    }



    public ram_Type getRam_type() {
        return ram_type;
    }

    public void setRam_type(ram_Type ram_type) {
        this.ram_type = ram_type;
    }
    public ram_Operation getRam_operation() {
        return ram_operation;
    }

    public void setRam_operation(ram_Operation ram_operation) {
        this.ram_operation = ram_operation;
    }

}