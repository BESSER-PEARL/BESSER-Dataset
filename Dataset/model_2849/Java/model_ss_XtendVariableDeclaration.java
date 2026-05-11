





import java.util.List;
import java.util.ArrayList;

public class model_ss_XtendVariableDeclaration extends XVariableDeclaration {

    private boolean extension;



    public model_ss_XtendVariableDeclaration(
        boolean extension    ) {
        super(
        );
        this.extension = extension;
    }


    public boolean getExtension() {
        return extension;
    }

    public void setExtension(boolean extension) {
        this.extension = extension;
    }


}