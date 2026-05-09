





import java.util.List;
import java.util.ArrayList;

public class PrimitiveTypes_Core_ISourceReference  {

    private String source;





    private Core_ISourceRange core_isourcerange;


    public PrimitiveTypes_Core_ISourceReference(
        String source    ) {
        this.source = source;
    }


    public String getSource() {
        return source;
    }

    public void setSource(String source) {
        this.source = source;
    }

    public Core_ISourceRange getCore_isourcerange() {
        return core_isourcerange;
    }

    public void setCore_isourcerange(Core_ISourceRange core_isourcerange) {
        this.core_isourcerange = core_isourcerange;
    }

}