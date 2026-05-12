





import java.util.List;
import java.util.ArrayList;

public class sqlmodel_datatypes_CharacterStringDataType extends PredefinedDataType {

    private boolean fixedLength;
    private String collationName;
    private String coercibility;
    private int length;





    private CharacterSet characterset;


    public sqlmodel_datatypes_CharacterStringDataType(
        boolean fixedLength,        String collationName,        String coercibility,        int length    ) {
        super(
        );
        this.fixedLength = fixedLength;
        this.collationName = collationName;
        this.coercibility = coercibility;
        this.length = length;
    }


    public boolean getFixedlength() {
        return fixedLength;
    }

    public void setFixedlength(boolean fixedLength) {
        this.fixedLength = fixedLength;
    }
    public String getCollationname() {
        return collationName;
    }

    public void setCollationname(String collationName) {
        this.collationName = collationName;
    }
    public String getCoercibility() {
        return coercibility;
    }

    public void setCoercibility(String coercibility) {
        this.coercibility = coercibility;
    }
    public int getLength() {
        return length;
    }

    public void setLength(int length) {
        this.length = length;
    }

    public CharacterSet getCharacterset() {
        return characterset;
    }

    public void setCharacterset(CharacterSet characterset) {
        this.characterset = characterset;
    }

}