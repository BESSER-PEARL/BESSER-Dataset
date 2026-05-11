





import java.util.List;
import java.util.ArrayList;

public class persistence_DataTypeAttribute extends EntityAttribute {

    private boolean obfuscateFormFields;
    private boolean caseInsensitive;
    private boolean encrypt;





    private persistence_DataType persistence_datatype;


    public persistence_DataTypeAttribute(
        boolean obfuscateFormFields,        boolean caseInsensitive,        boolean encrypt    ) {
        super(
        );
        this.obfuscateFormFields = obfuscateFormFields;
        this.caseInsensitive = caseInsensitive;
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
    public boolean getEncrypt() {
        return encrypt;
    }

    public void setEncrypt(boolean encrypt) {
        this.encrypt = encrypt;
    }

    public persistence_DataType getPersistence_datatype() {
        return persistence_datatype;
    }

    public void setPersistence_datatype(persistence_DataType persistence_datatype) {
        this.persistence_datatype = persistence_datatype;
    }

}