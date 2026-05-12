





import java.util.List;
import java.util.ArrayList;

public class relational_ProcedureParameter extends RelationalEntity {

    private int scale;
    private int precision;
    private String nativeType;
    private int length;
    private String direction;
    private String nullable;
    private String defaultValue;
    private int radix;



    public relational_ProcedureParameter(
        int scale,        int precision,        String nativeType,        int length,        String direction,        String nullable,        String defaultValue,        int radix    ) {
        super(
        );
        this.scale = scale;
        this.precision = precision;
        this.nativeType = nativeType;
        this.length = length;
        this.direction = direction;
        this.nullable = nullable;
        this.defaultValue = defaultValue;
        this.radix = radix;
    }


    public int getScale() {
        return scale;
    }

    public void setScale(int scale) {
        this.scale = scale;
    }
    public int getPrecision() {
        return precision;
    }

    public void setPrecision(int precision) {
        this.precision = precision;
    }
    public String getNativetype() {
        return nativeType;
    }

    public void setNativetype(String nativeType) {
        this.nativeType = nativeType;
    }
    public int getLength() {
        return length;
    }

    public void setLength(int length) {
        this.length = length;
    }
    public String getDirection() {
        return direction;
    }

    public void setDirection(String direction) {
        this.direction = direction;
    }
    public String getNullable() {
        return nullable;
    }

    public void setNullable(String nullable) {
        this.nullable = nullable;
    }
    public String getDefaultvalue() {
        return defaultValue;
    }

    public void setDefaultvalue(String defaultValue) {
        this.defaultValue = defaultValue;
    }
    public int getRadix() {
        return radix;
    }

    public void setRadix(int radix) {
        this.radix = radix;
    }


}