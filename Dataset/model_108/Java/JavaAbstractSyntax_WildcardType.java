





import java.util.List;
import java.util.ArrayList;

public class JavaAbstractSyntax_WildcardType extends Type {

    private String upperBound;



    public JavaAbstractSyntax_WildcardType(
        String upperBound    ) {
        super(
        );
        this.upperBound = upperBound;
    }


    public String getUpperbound() {
        return upperBound;
    }

    public void setUpperbound(String upperBound) {
        this.upperBound = upperBound;
    }


}