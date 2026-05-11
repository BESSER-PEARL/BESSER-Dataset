





import java.util.List;
import java.util.ArrayList;

public class afpText_ExtendedResourceLocalIdentifier extends triplet {

    private String ResLID;
    private String ResType;



    public afpText_ExtendedResourceLocalIdentifier(
        String ResLID,        String ResType    ) {
        super(
        );
        this.ResLID = ResLID;
        this.ResType = ResType;
    }


    public String getReslid() {
        return ResLID;
    }

    public void setReslid(String ResLID) {
        this.ResLID = ResLID;
    }
    public String getRestype() {
        return ResType;
    }

    public void setRestype(String ResType) {
        this.ResType = ResType;
    }


}