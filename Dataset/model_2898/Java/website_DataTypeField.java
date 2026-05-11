





import java.util.List;
import java.util.ArrayList;

public class website_DataTypeField extends InterfaceField {

    private boolean encrypt;
    private boolean obfuscateFormFields;
    private String interfaceType;





    private website_DataType website_datatype;


    public website_DataTypeField(
        boolean encrypt,        boolean obfuscateFormFields,        String interfaceType    ) {
        super(
        );
        this.encrypt = encrypt;
        this.obfuscateFormFields = obfuscateFormFields;
        this.interfaceType = interfaceType;
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
    public String getInterfacetype() {
        return interfaceType;
    }

    public void setInterfacetype(String interfaceType) {
        this.interfaceType = interfaceType;
    }

    public website_DataType getWebsite_datatype() {
        return website_datatype;
    }

    public void setWebsite_datatype(website_DataType website_datatype) {
        this.website_datatype = website_datatype;
    }

}