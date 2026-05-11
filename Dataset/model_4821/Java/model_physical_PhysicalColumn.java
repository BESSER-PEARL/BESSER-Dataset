





import java.util.List;
import java.util.ArrayList;

public class model_physical_PhysicalColumn extends ModelObject {

    private String comment;
    private int size;
    private int position;
    private boolean nullable;
    private int decimalDigits;
    private String defaultValue;
    private String typeName;
    private int radix;
    private String dataType;
    private int octectLength;



    public model_physical_PhysicalColumn(
        String comment,        int size,        int position,        boolean nullable,        int decimalDigits,        String defaultValue,        String typeName,        int radix,        String dataType,        int octectLength    ) {
        super(
        );
        this.comment = comment;
        this.size = size;
        this.position = position;
        this.nullable = nullable;
        this.decimalDigits = decimalDigits;
        this.defaultValue = defaultValue;
        this.typeName = typeName;
        this.radix = radix;
        this.dataType = dataType;
        this.octectLength = octectLength;
    }


    public String getComment() {
        return comment;
    }

    public void setComment(String comment) {
        this.comment = comment;
    }
    public int getSize() {
        return size;
    }

    public void setSize(int size) {
        this.size = size;
    }
    public int getPosition() {
        return position;
    }

    public void setPosition(int position) {
        this.position = position;
    }
    public boolean getNullable() {
        return nullable;
    }

    public void setNullable(boolean nullable) {
        this.nullable = nullable;
    }
    public int getDecimaldigits() {
        return decimalDigits;
    }

    public void setDecimaldigits(int decimalDigits) {
        this.decimalDigits = decimalDigits;
    }
    public String getDefaultvalue() {
        return defaultValue;
    }

    public void setDefaultvalue(String defaultValue) {
        this.defaultValue = defaultValue;
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
    public String getDatatype() {
        return dataType;
    }

    public void setDatatype(String dataType) {
        this.dataType = dataType;
    }
    public int getOctectlength() {
        return octectLength;
    }

    public void setOctectlength(int octectLength) {
        this.octectLength = octectLength;
    }


}