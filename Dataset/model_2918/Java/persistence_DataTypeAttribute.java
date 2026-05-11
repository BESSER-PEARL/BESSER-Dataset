





import java.util.List;
import java.util.ArrayList;

public class persistence_DataTypeAttribute extends EntityAttribute {

    private boolean obfuscateFormFields;
    private boolean encrypt;
    private boolean caseInsensitive;





    private persistence_DataType persistence_datatype;


    public persistence_DataTypeAttribute(
        boolean obfuscateFormFields,        boolean encrypt,        boolean caseInsensitive    ) {
        super(
        );
        this.obfuscateFormFields = obfuscateFormFields;
        this.encrypt = encrypt;
        this.caseInsensitive = caseInsensitive;
    }


    public boolean getObfuscateformfields() {
        return obfuscateFormFields;
    }

    public void setObfuscateformfields(boolean obfuscateFormFields) {
        this.obfuscateFormFields = obfuscateFormFields;
    }
    public boolean getEncrypt() {
        return encrypt;
    }

    public void setEncrypt(boolean encrypt) {
        this.encrypt = encrypt;
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