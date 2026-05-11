





import java.util.List;
import java.util.ArrayList;

public class optGrammar_Type  {

    private boolean isVarType;





    private optGrammar_ReturnParameterDeclaration optgrammar_returnparameterdeclaration;




    private optGrammar_Mapping optgrammar_mapping;


    public optGrammar_Type(
        boolean isVarType    ) {
        this.isVarType = isVarType;
    }


    public boolean getIsvartype() {
        return isVarType;
    }

    public void setIsvartype(boolean isVarType) {
        this.isVarType = isVarType;
    }

    public optGrammar_ReturnParameterDeclaration getOptgrammar_returnparameterdeclaration() {
        return optgrammar_returnparameterdeclaration;
    }

    public void setOptgrammar_returnparameterdeclaration(optGrammar_ReturnParameterDeclaration optgrammar_returnparameterdeclaration) {
        this.optgrammar_returnparameterdeclaration = optgrammar_returnparameterdeclaration;
    }
    public optGrammar_Mapping getOptgrammar_mapping() {
        return optgrammar_mapping;
    }

    public void setOptgrammar_mapping(optGrammar_Mapping optgrammar_mapping) {
        this.optgrammar_mapping = optgrammar_mapping;
    }

}