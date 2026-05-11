





import java.util.List;
import java.util.ArrayList;

public class persistence_DataTypeAttribute extends Attribute {

    private boolean encrypt;
    private boolean obfuscateFormFields;
    private boolean caseInsensitive;





    private persistence_DataType persistence_datatype;


    public persistence_DataTypeAttribute(
        boolean encrypt,        boolean obfuscateFormFields,        boolean caseInsensitive    ) {
        super(
        );
        this.encrypt = encrypt;
        this.obfuscateFormFields = obfuscateFormFields;
        this.caseInsensitive = caseInsensitive;
    }


    public boolean getEncrypt() {
        return encrypt;
    }

    public void setEncrypt(boolean encrypt) {
        this.encrypt = encrypt;
    }
    public boolean getObfuscateformfields() {
        return obfuscateFormFields;
    }

    public void setObfuscateformfields(boolean obfuscateFormFields) {
        this.obfuscateFormFields = obfuscateFormFields;
    }
    public boolean getCaseinsensitive() {
        return caseInsensitive;
    }

    public void setCaseinsensitive(boolean caseInsensitive) {
        this.caseInsensitive = caseInsensitive;
    }

    public persistence_DataType getPersistence_datatype() {
        return persistence_datatype;
    }

    public void setPersistence_datatype(persistence_DataType persistence_datatype) {
        this.persistence_datatype = persistence_datatype;
    }

}