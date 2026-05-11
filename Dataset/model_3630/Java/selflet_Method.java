





import java.util.List;
import java.util.ArrayList;

public class selflet_Method  {

    private String name;
    private String paramType;



    public selflet_Method(
        String name,        String paramType    ) {
        this.name = name;
        this.paramType = paramType;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getParamtype() {
        return paramType;
    }

    public void setParamtype(String paramType) {
        this.paramType = paramType;
    }


}