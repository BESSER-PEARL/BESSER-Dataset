





import java.util.List;
import java.util.ArrayList;

public class haxe_HaxeAbstractOperation extends HaxeAbstractFunction {

    private boolean overrides;
    private boolean isInline;





    private haxe_HaxeAbstractMethodInvocation haxe_haxeabstractmethodinvocation;


    public haxe_HaxeAbstractOperation(
        boolean overrides,        boolean isInline    ) {
        super(
        );
        this.overrides = overrides;
        this.isInline = isInline;
    }


    public boolean getOverrides() {
        return overrides;
    }

    public void setOverrides(boolean overrides) {
        this.overrides = overrides;
    }
    public boolean getIsinline() {
        return isInline;
    }

    public void setIsinline(boolean isInline) {
        this.isInline = isInline;
    }

    public haxe_HaxeAbstractMethodInvocation getHaxe_haxeabstractmethodinvocation() {
        return haxe_haxeabstractmethodinvocation;
    }

    public void setHaxe_haxeabstractmethodinvocation(haxe_HaxeAbstractMethodInvocation haxe_haxeabstractmethodinvocation) {
        this.haxe_haxeabstractmethodinvocation = haxe_haxeabstractmethodinvocation;
    }

}