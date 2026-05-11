





import java.util.List;
import java.util.ArrayList;

public class vcml_FormattedDocumentationBlock  {

    private String format;
    private String value;





    private vcml_MultipleLanguageDocumentation_LanguageBlock vcml_multiplelanguagedocumentation_languageblock;


    public vcml_FormattedDocumentationBlock(
        String format,        String value    ) {
        this.format = format;
        this.value = value;
    }


    public String getFormat() {
        return format;
    }

    public void setFormat(String format) {
        this.format = format;
    }
    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }

    public vcml_MultipleLanguageDocumentation_LanguageBlock getVcml_multiplelanguagedocumentation_languageblock() {
        return vcml_multiplelanguagedocumentation_languageblock;
    }

    public void setVcml_multiplelanguagedocumentation_languageblock(vcml_MultipleLanguageDocumentation_LanguageBlock vcml_multiplelanguagedocumentation_languageblock) {
        this.vcml_multiplelanguagedocumentation_languageblock = vcml_multiplelanguagedocumentation_languageblock;
    }

}