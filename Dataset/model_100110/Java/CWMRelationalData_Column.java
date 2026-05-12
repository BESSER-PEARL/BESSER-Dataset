





import java.util.List;
import java.util.ArrayList;

public class CWMRelationalData_Column  {

    private String length;
    private String isNullable;
    private String characterSetName;
    private String scale;
    private String precision;
    private String collectionName;



    public CWMRelationalData_Column(
        String length,        String isNullable,        String characterSetName,        String scale,        String precision,        String collectionName    ) {
        this.length = length;
        this.isNullable = isNullable;
        this.characterSetName = characterSetName;
        this.scale = scale;
        this.precision = precision;
        this.collectionName = collectionName;
    }


    public String getLength() {
        return length;
    }

    public void setLength(String length) {
        this.length = length;
    }
    public String getIsnullable() {
        return isNullable;
    }

    public void setIsnullable(String isNullable) {
        this.isNullable = isNullable;
    }
    public String getCharactersetname() {
        return characterSetName;
    }

    public void setCharactersetname(String characterSetName) {
        this.characterSetName = characterSetName;
    }
    public String getScale() {
        return scale;
    }

    public void setScale(String scale) {
        this.scale = scale;
    }
    public String getPrecision() {
        return precision;
    }

    public void setPrecision(String precision) {
        this.precision = precision;
    }
    public String getCollectionname() {
        return collectionName;
    }

    public void setCollectionname(String collectionName) {
        this.collectionName = collectionName;
    }


}