





import java.util.List;
import java.util.ArrayList;

public class PhotosMetaModel_ReactDOM extends ReactConfiguration {

    private String isStruct;
    private String isRoute;
    private String isConstant;



    public PhotosMetaModel_ReactDOM(
        String isStruct,        String isRoute,        String isConstant    ) {
        super(
        );
        this.isStruct = isStruct;
        this.isRoute = isRoute;
        this.isConstant = isConstant;
    }


    public String getIsstruct() {
        return isStruct;
    }

    public void setIsstruct(String isStruct) {
        this.isStruct = isStruct;
    }
    public String getIsroute() {
        return isRoute;
    }

    public void setIsroute(String isRoute) {
        this.isRoute = isRoute;
    }
    public String getIsconstant() {
        return isConstant;
    }

    public void setIsconstant(String isConstant) {
        this.isConstant = isConstant;
    }


}