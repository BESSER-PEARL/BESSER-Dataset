





import java.util.List;
import java.util.ArrayList;

public class Core_IClassFile extends ITypeRoot {

    private String isInterface;
    private String isClass;



    public Core_IClassFile(
        String isInterface,        String isClass    ) {
        super(
        );
        this.isInterface = isInterface;
        this.isClass = isClass;
    }


    public String getIsinterface() {
        return isInterface;
    }

    public void setIsinterface(String isInterface) {
        this.isInterface = isInterface;
    }
    public String getIsclass() {
        return isClass;
    }

    public void setIsclass(String isClass) {
        this.isClass = isClass;
    }


}