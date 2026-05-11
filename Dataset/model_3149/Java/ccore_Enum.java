





import java.util.List;
import java.util.ArrayList;

public class ccore_Enum extends Attribute {

    private String enumClazz;
    private String values;



    public ccore_Enum(
        String enumClazz,        String values    ) {
        super(
        );
        this.enumClazz = enumClazz;
        this.values = values;
    }


    public String getEnumclazz() {
        return enumClazz;
    }

    public void setEnumclazz(String enumClazz) {
        this.enumClazz = enumClazz;
    }
    public String getValues() {
        return values;
    }

    public void setValues(String values) {
        this.values = values;
    }


}