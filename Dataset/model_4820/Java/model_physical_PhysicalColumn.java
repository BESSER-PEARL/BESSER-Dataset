





import java.util.List;
import java.util.ArrayList;

public class model_physical_PhysicalColumn extends ModelObject {

    private String typeName;
    private int radix;
    private String comment;
    private String dataType;
    private String defaultValue;
    private int size;
    private boolean nullable;
    private int position;
    private int decimalDigits;
    private int octectLength;



    public model_physical_PhysicalColumn(
        String typeName,        int radix,        String comment,        String dataType,        String defaultValue,        int size,        boolean nullable,        int position,        int decimalDigits,        int octectLength    ) {
        super(
        );
        this.typeName = typeName;
        this.radix = radix;
        this.comment = comment;
        this.dataType = dataType;
        this.defaultValue = defaultValue;
        this.size = size;
        this.nullable = nullable;
        this.position = position;
        this.decimalDigits = decimalDigits;
        this.octectLength = octectLength;
    }


    public String getTypename() {
        return typeName;
    }

    public void setTypename(String typeName) {
        this.typeName = typeName;
    }
    public int getRadix() {
        return radix;
    }

    public void setRadix(int radix) {
        this.radix = radix;
    }
    public String getComment() {
        return comment;
    }

    public void setComment(String comment) {
        this.comment = comment;
    }
    public String getDatatype() {
        return dataType;
    }

    public void setDatatype(String dataType) {
        this.dataType = dataType;
    }
    public String getDefaultvalue() {
        return defaultValue;
    }

    public void setDefaultvalue(String defaultValue) {
        this.defaultValue = defaultValue;
    }
    public int getSize() {
        return size;
    }

    public void setSize(int size) {
        this.size = size;
    }
    public boolean getNullable() {
        return nullable;
    }

    public void setNullable(boolean nullable) {
        this.nullable = nullable;
    }
    public int getPosition() {
        return position;
    }

    public void setPosition(int position) {
        this.position = position;
    }
    public int getDecimaldigits() {
        return decimalDigits;
    }

    public void setDecimaldigits(int decimalDigits) {
        this.decimalDigits = decimalDigits;
    }
    public int getOctectlength() {
        return octectLength;
    }

    public void setOctectlength(int octectLength) {
        this.octectLength = octectLength;
    }


}