





import java.util.List;
import java.util.ArrayList;

public class afpText_FullyQualifiedName extends triplet {

    private String FQNFormat;
    private String FQName;
    private String FQNType;



    public afpText_FullyQualifiedName(
        String FQNFormat,        String FQName,        String FQNType    ) {
        super(
        );
        this.FQNFormat = FQNFormat;
        this.FQName = FQName;
        this.FQNType = FQNType;
    }


    public String getFqnformat() {
        return FQNFormat;
    }

    public void setFqnformat(String FQNFormat) {
        this.FQNFormat = FQNFormat;
    }
    public String getFqname() {
        return FQName;
    }

    public void setFqname(String FQName) {
        this.FQName = FQName;
    }
    public String getFqntype() {
        return FQNType;
    }

    public void setFqntype(String FQNType) {
        this.FQNType = FQNType;
    }


}