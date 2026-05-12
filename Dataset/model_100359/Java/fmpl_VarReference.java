





import java.util.List;
import java.util.ArrayList;

public class fmpl_VarReference extends Expression {






    private fmpl_VarDeclaration fmpl_vardeclaration;




    private fmpl_Write fmpl_write;


    public fmpl_VarReference(
    ) {
        super(
        );
    }



    public fmpl_VarDeclaration getFmpl_vardeclaration() {
        return fmpl_vardeclaration;
    }

    public void setFmpl_vardeclaration(fmpl_VarDeclaration fmpl_vardeclaration) {
        this.fmpl_vardeclaration = fmpl_vardeclaration;
    }
    public fmpl_Write getFmpl_write() {
        return fmpl_write;
    }

    public void setFmpl_write(fmpl_Write fmpl_write) {
        this.fmpl_write = fmpl_write;
    }

}