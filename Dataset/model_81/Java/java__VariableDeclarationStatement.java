





import java.util.List;
import java.util.ArrayList;

public class java__VariableDeclarationStatement extends Statement, AbstractVariablesContainer {

    private int extraArrayDimensions;



    public java__VariableDeclarationStatement(
        int extraArrayDimensions    ) {
        super(
        );
        this.extraArrayDimensions = extraArrayDimensions;
    }


    public int getExtraarraydimensions() {
        return extraArrayDimensions;
    }

    public void setExtraarraydimensions(int extraArrayDimensions) {
        this.extraArrayDimensions = extraArrayDimensions;
    }


}