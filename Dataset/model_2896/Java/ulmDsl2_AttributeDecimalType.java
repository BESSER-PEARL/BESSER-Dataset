





import java.util.List;
import java.util.ArrayList;

public class ulmDsl2_AttributeDecimalType  {

    private String name;
    private int scale;
    private boolean array;
    private int precision;



    public ulmDsl2_AttributeDecimalType(
        String name,        int scale,        boolean array,        int precision    ) {
        this.name = name;
        this.scale = scale;
        this.array = array;
        this.precision = precision;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public int getScale() {
        return scale;
    }

    public void setScale(int scale) {
        this.scale = scale;
    }
    public boolean getArray() {
        return array;
    }

    public void setArray(boolean array) {
        this.array = array;
    }
    public int getPrecision() {
        return precision;
    }

    public void setPrecision(int precision) {
        this.precision = precision;
    }


}