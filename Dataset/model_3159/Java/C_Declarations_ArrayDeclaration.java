





import java.util.List;
import java.util.ArrayList;

public class C_Declarations_ArrayDeclaration extends Abstractions_BlockedElement, Declarations_CompositeVariableDeclaration {

    private String dimensions;



    public C_Declarations_ArrayDeclaration(
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