





import java.util.List;
import java.util.ArrayList;

public class service_BusinessOperation extends FormalParameterList, NamedElement {

    private String resultType;
    private String resultMimeType;



    public service_BusinessOperation(
        String resultType,        String resultMimeType    ) {
        super(
        );
        this.resultType = resultType;
        this.resultMimeType = resultMimeType;
    }


    public String getResulttype() {
        return resultType;
    }

    public void setResulttype(String resultType) {
        this.resultType = resultType;
    }
    public String getResultmimetype() {
        return resultMimeType;
    }

    public void setResultmimetype(String resultMimeType) {
        this.resultMimeType = resultMimeType;
    }


}