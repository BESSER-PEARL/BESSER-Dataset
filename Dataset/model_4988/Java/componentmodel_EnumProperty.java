





import java.util.List;
import java.util.ArrayList;

public class componentmodel_EnumProperty extends Property {

    private String literalValue;



    public componentmodel_EnumProperty(
        String literalValue    ) {
        super(
        );
        this.literalValue = literalValue;
    }


    public String getLiteralvalue() {
        return literalValue;
    }

    public void setLiteralvalue(String literalValue) {
        this.literalValue = literalValue;
    }


}