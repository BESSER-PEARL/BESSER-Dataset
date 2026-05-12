





import java.util.List;
import java.util.ArrayList;

public class relationaldatabase_Column extends NamedElement {

    private boolean nullable;
    private String scale;
    private boolean primaryKey;
    private String size;
    private int arrayDimensions;
    private boolean unique;



    public relationaldatabase_Column(
        boolean nullable,        String scale,        boolean primaryKey,        String size,        int arrayDimensions,        boolean unique    ) {
        super(
        );
        this.nullable = nullable;
        this.scale = scale;
        this.primaryKey = primaryKey;
        this.size = size;
        this.arrayDimensions = arrayDimensions;
        this.unique = unique;
    }


    public boolean getNullable() {
        return nullable;
    }

    public void setNullable(boolean nullable) {
        this.nullable = nullable;
    }
    public String getScale() {
        return scale;
    }

    public void setScale(String scale) {
        this.scale = scale;
    }
    public boolean getPrimarykey() {
        return primaryKey;
    }

    public void setPrimarykey(boolean primaryKey) {
        this.primaryKey = primaryKey;
    }
    public String getSize() {
        return size;
    }

    public void setSize(String size) {
        this.size = size;
    }
    public int getArraydimensions() {
        return arrayDimensions;
    }

    public void setArraydimensions(int arrayDimensions) {
        this.arrayDimensions = arrayDimensions;
    }
    public boolean getUnique() {
        return unique;
    }

    public void setUnique(boolean unique) {
        this.unique = unique;
    }


}