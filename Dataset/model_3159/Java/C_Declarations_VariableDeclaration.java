





import java.util.List;
import java.util.ArrayList;

public class C_Declarations_VariableDeclaration extends Declaration {

    private String numberOfPointers;
    private String isAPointer;



    public C_Declarations_VariableDeclaration(
        String numberOfPointers,        String isAPointer    ) {
        super(
        );
        this.numberOfPointers = numberOfPointers;
        this.isAPointer = isAPointer;
    }


    public String getNumberofpointers() {
        return numberOfPointers;
    }

    public void setNumberofpointers(String numberOfPointers) {
        this.numberOfPointers = numberOfPointers;
    }
    public String getIsapointer() {
        return isAPointer;
    }

    public void setIsapointer(String isAPointer) {
        this.isAPointer = isAPointer;
    }


}