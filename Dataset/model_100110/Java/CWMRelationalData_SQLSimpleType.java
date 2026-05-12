





import java.util.List;
import java.util.ArrayList;

public class CWMRelationalData_SQLSimpleType extends SQLDataType {

    private String characterOctetLength;
    private String characterMaximumLength;
    private String numericPrecisionRadix;
    private String dateTimePrecision;
    private String numericScale;
    private String numericPrecision;



    public CWMRelationalData_SQLSimpleType(
        String characterOctetLength,        String characterMaximumLength,        String numericPrecisionRadix,        String dateTimePrecision,        String numericScale,        String numericPrecision    ) {
        super(
        );
        this.characterOctetLength = characterOctetLength;
        this.characterMaximumLength = characterMaximumLength;
        this.numericPrecisionRadix = numericPrecisionRadix;
        this.dateTimePrecision = dateTimePrecision;
        this.numericScale = numericScale;
        this.numericPrecision = numericPrecision;
    }


    public String getCharacteroctetlength() {
        return characterOctetLength;
    }

    public void setCharacteroctetlength(String characterOctetLength) {
        this.characterOctetLength = characterOctetLength;
    }
    public String getCharactermaximumlength() {
        return characterMaximumLength;
    }

    public void setCharactermaximumlength(String characterMaximumLength) {
        this.characterMaximumLength = characterMaximumLength;
    }
    public String getNumericprecisionradix() {
        return numericPrecisionRadix;
    }

    public void setNumericprecisionradix(String numericPrecisionRadix) {
        this.numericPrecisionRadix = numericPrecisionRadix;
    }
    public String getDatetimeprecision() {
        return dateTimePrecision;
    }

    public void setDatetimeprecision(String dateTimePrecision) {
        this.dateTimePrecision = dateTimePrecision;
    }
    public String getNumericscale() {
        return numericScale;
    }

    public void setNumericscale(String numericScale) {
        this.numericScale = numericScale;
    }
    public String getNumericprecision() {
        return numericPrecision;
    }

    public void setNumericprecision(String numericPrecision) {
        this.numericPrecision = numericPrecision;
    }


}