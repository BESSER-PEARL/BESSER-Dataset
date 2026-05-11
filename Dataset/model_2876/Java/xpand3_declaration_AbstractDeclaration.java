





import java.util.List;
import java.util.ArrayList;

public class xpand3_declaration_AbstractDeclaration extends SyntaxElement {

    private boolean isPrivate;



    public xpand3_declaration_AbstractDeclaration(
        boolean isPrivate    ) {
        super(
        );
        this.isPrivate = isPrivate;
    }


    public boolean getIsprivate() {
        return isPrivate;
    }

    public void setIsprivate(boolean isPrivate) {
        this.isPrivate = isPrivate;
    }


}