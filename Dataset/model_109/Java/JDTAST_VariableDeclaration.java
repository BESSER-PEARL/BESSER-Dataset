





import java.util.List;
import java.util.ArrayList;

public class JDTAST_VariableDeclaration extends ASTNode {

    private String extraDimensions;



    public JDTAST_VariableDeclaration(
        String extraDimensions    ) {
        super(
        );
        this.extraDimensions = extraDimensions;
    }


    public String getExtradimensions() {
        return extraDimensions;
    }

    public void setExtradimensions(String extraDimensions) {
        this.extraDimensions = extraDimensions;
    }


}