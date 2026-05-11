





import java.util.List;
import java.util.ArrayList;

public class haxe_HaxeAttribute extends HaxeField, HaxeSingleVariableDeclaration {

    private String setterProperty;
    private String getterProperty;





    private haxe_HaxeClassifier haxe_haxeclassifier;




    private haxe_HaxeOperation haxe_haxeoperation;




    private haxe_HaxeOperation haxe_haxeoperation;


    public haxe_HaxeAttribute(
        String setterProperty,        String getterProperty    ) {
        super(
        );
        this.setterProperty = setterProperty;
        this.getterProperty = getterProperty;
    }


    public String getSetterproperty() {
        return setterProperty;
    }

    public void setSetterproperty(String setterProperty) {
        this.setterProperty = setterProperty;
    }
    public String getGetterproperty() {
        return getterProperty;
    }

    public void setGetterproperty(String getterProperty) {
        this.getterProperty = getterProperty;
    }

    public haxe_HaxeClassifier getHaxe_haxeclassifier() {
        return haxe_haxeclassifier;
    }

    public void setHaxe_haxeclassifier(haxe_HaxeClassifier haxe_haxeclassifier) {
        this.haxe_haxeclassifier = haxe_haxeclassifier;
    }
    public haxe_HaxeOperation getHaxe_haxeoperation() {
        return haxe_haxeoperation;
    }

    public void setHaxe_haxeoperation(haxe_HaxeOperation haxe_haxeoperation) {
        this.haxe_haxeoperation = haxe_haxeoperation;
    }
    public haxe_HaxeOperation getHaxe_haxeoperation() {
        return haxe_haxeoperation;
    }

    public void setHaxe_haxeoperation(haxe_HaxeOperation haxe_haxeoperation) {
        this.haxe_haxeoperation = haxe_haxeoperation;
    }

}