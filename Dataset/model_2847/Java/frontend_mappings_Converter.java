





import java.util.List;
import java.util.ArrayList;

public class frontend_mappings_Converter  {

    private String converterName;
    private String isExternal;





    private UseDeclaration usedeclaration;


    public frontend_mappings_Converter(
        String converterName,        String isExternal    ) {
        this.converterName = converterName;
        this.isExternal = isExternal;
    }


    public String getConvertername() {
        return converterName;
    }

    public void setConvertername(String converterName) {
        this.converterName = converterName;
    }
    public String getIsexternal() {
        return isExternal;
    }

    public void setIsexternal(String isExternal) {
        this.isExternal = isExternal;
    }

    public UseDeclaration getUsedeclaration() {
        return usedeclaration;
    }

    public void setUsedeclaration(UseDeclaration usedeclaration) {
        this.usedeclaration = usedeclaration;
    }

}