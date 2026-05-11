





import java.util.List;
import java.util.ArrayList;

public class room_PrimitiveType extends DataType {

    private String castName;
    private String defaultValueLiteral;
    private String targetName;



    public room_PrimitiveType(
        String castName,        String defaultValueLiteral,        String targetName    ) {
        super(
        );
        this.castName = castName;
        this.defaultValueLiteral = defaultValueLiteral;
        this.targetName = targetName;
    }


    public String getCastname() {
        return castName;
    }

    public void setCastname(String castName) {
        this.castName = castName;
    }
    public String getDefaultvalueliteral() {
        return defaultValueLiteral;
    }

    public void setDefaultvalueliteral(String defaultValueLiteral) {
        this.defaultValueLiteral = defaultValueLiteral;
    }
    public String getTargetname() {
        return targetName;
    }

    public void setTargetname(String targetName) {
        this.targetName = targetName;
    }


}