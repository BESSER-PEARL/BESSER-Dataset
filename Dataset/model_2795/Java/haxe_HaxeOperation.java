





import java.util.List;
import java.util.ArrayList;

public class haxe_HaxeOperation extends HaxeAbstractOperation, HaxeField, HaxeTypedElement {

    private boolean macro;



    public haxe_HaxeOperation(
        boolean macro    ) {
        super(
        );
        this.macro = macro;
    }


    public boolean getMacro() {
        return macro;
    }

    public void setMacro(boolean macro) {
        this.macro = macro;
    }


}