





import java.util.List;
import java.util.ArrayList;

public class ccore_EnumType extends EEnum {

    private String values;
    private String javaClass;
    private boolean mustBeGenerated;





    private ccore_Enum ccore_enum;


    public ccore_EnumType(
        String values,        String javaClass,        boolean mustBeGenerated    ) {
        super(
        );
        this.values = values;
        this.javaClass = javaClass;
        this.mustBeGenerated = mustBeGenerated;
    }


    public String getValues() {
        return values;
    }

    public void setValues(String values) {
        this.values = values;
    }
    public String getJavaclass() {
        return javaClass;
    }

    public void setJavaclass(String javaClass) {
        this.javaClass = javaClass;
    }
    public boolean getMustbegenerated() {
        return mustBeGenerated;
    }

    public void setMustbegenerated(boolean mustBeGenerated) {
        this.mustBeGenerated = mustBeGenerated;
    }

    public ccore_Enum getCcore_enum() {
        return ccore_enum;
    }

    public void setCcore_enum(ccore_Enum ccore_enum) {
        this.ccore_enum = ccore_enum;
    }

}