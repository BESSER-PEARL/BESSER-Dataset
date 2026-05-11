





import java.util.List;
import java.util.ArrayList;

public class haxe_HaxeStringLiteral extends HaxeConstant {

    private String escapedValue;



    public haxe_HaxeStringLiteral(
        String escapedValue    ) {
        super(
        );
        this.escapedValue = escapedValue;
    }


    public String getEscapedvalue() {
        return escapedValue;
    }

    public void setEscapedvalue(String escapedValue) {
        this.escapedValue = escapedValue;
    }


}