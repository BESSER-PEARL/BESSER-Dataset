





import java.util.List;
import java.util.ArrayList;

public class architectureTool_Method  {

    private String parameter;
    private String visable;
    private String name;
    private String returnType;



    public architectureTool_Method(
        String parameter,        String visable,        String name,        String returnType    ) {
        this.parameter = parameter;
        this.visable = visable;
        this.name = name;
        this.returnType = returnType;
    }


    public String getParameter() {
        return parameter;
    }

    public void setParameter(String parameter) {
        this.parameter = parameter;
    }
    public String getVisable() {
        return visable;
    }

    public void setVisable(String visable) {
        this.visable = visable;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getReturntype() {
        return returnType;
    }

    public void setReturntype(String returnType) {
        this.returnType = returnType;
    }


}