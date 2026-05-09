





import java.util.List;
import java.util.ArrayList;

public class rapidml_EnumConstant extends Documentable {

    private int integerValue;
    private String literalValue;
    private String name;



    public rapidml_EnumConstant(
        int integerValue,        String literalValue,        String name    ) {
        super(
        );
        this.integerValue = integerValue;
        this.literalValue = literalValue;
        this.name = name;
    }


    public int getIntegervalue() {
        return integerValue;
    }

    public void setIntegervalue(int integerValue) {
        this.integerValue = integerValue;
    }
    public String getLiteralvalue() {
        return literalValue;
    }

    public void setLiteralvalue(String literalValue) {
        this.literalValue = literalValue;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}