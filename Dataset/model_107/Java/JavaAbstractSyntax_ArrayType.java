





import java.util.List;
import java.util.ArrayList;

public class JavaAbstractSyntax_ArrayType extends Type {

    private String dimensions;



    public JavaAbstractSyntax_ArrayType(
        String dimensions    ) {
        super(
        );
        this.dimensions = dimensions;
    }


    public String getDimensions() {
        return dimensions;
    }

    public void setDimensions(String dimensions) {
        this.dimensions = dimensions;
    }


}