





import java.util.List;
import java.util.ArrayList;

public class ir_IrAnnotation  {

    private String source;





    private ir_IrAnnotable ir_irannotable;


    public ir_IrAnnotation(
        String source    ) {
        this.source = source;
    }


    public String getSource() {
        return source;
    }

    public void setSource(String source) {
        this.source = source;
    }

    public ir_IrAnnotable getIr_irannotable() {
        return ir_irannotable;
    }

    public void setIr_irannotable(ir_IrAnnotable ir_irannotable) {
        this.ir_irannotable = ir_irannotable;
    }

}