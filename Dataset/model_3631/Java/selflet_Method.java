





import java.util.List;
import java.util.ArrayList;

public class selflet_Method  {

    private String paramType;
    private String name;



    public selflet_Method(
        String paramType,        String name    ) {
        this.paramType = paramType;
        this.name = name;
    }


    public String getParamtype() {
        return paramType;
    }

    public void setParamtype(String paramType) {
        this.paramType = paramType;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}