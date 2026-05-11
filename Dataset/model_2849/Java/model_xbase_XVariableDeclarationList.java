





import java.util.List;
import java.util.ArrayList;

public class model_xbase_XVariableDeclarationList extends XExpression {

    private boolean exported;
    private boolean writeable;



    public model_xbase_XVariableDeclarationList(
        boolean exported,        boolean writeable    ) {
        super(
        );
        this.exported = exported;
        this.writeable = writeable;
    }


    public boolean getExported() {
        return exported;
    }

    public void setExported(boolean exported) {
        this.exported = exported;
    }
    public boolean getWriteable() {
        return writeable;
    }

    public void setWriteable(boolean writeable) {
        this.writeable = writeable;
    }


}