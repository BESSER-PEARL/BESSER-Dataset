





import java.util.List;
import java.util.ArrayList;

public class Core_IClassFile extends ITypeRoot {

    private String isClass;
    private String isInterface;



    public Core_IClassFile(
        String isClass,        String isInterface    ) {
        super(
        );
        this.isClass = isClass;
        this.isInterface = isInterface;
    }


    public String getIsclass() {
        return isClass;
    }

    public void setIsclass(String isClass) {
        this.isClass = isClass;
    }
    public String getIsinterface() {
        return isInterface;
    }

    public void setIsinterface(String isInterface) {
        this.isInterface = isInterface;
    }


}