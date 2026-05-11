





import java.util.List;
import java.util.ArrayList;

public class website_DataTypeAttribute extends EntityAttribute {

    private boolean obfuscateFormFields;
    private boolean encrypt;
    private boolean caseInsensitive;





    private website_DataType website_datatype;


    public website_DataTypeAttribute(
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

    public website_DataType getWebsite_datatype() {
        return website_datatype;
    }

    public void setWebsite_datatype(website_DataType website_datatype) {
        this.website_datatype = website_datatype;
    }

}