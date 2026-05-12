





import java.util.List;
import java.util.ArrayList;

public class HTML_PARAM  {

    private String paramValue;
    private String name;



    public HTML_PARAM(
        String paramValue,        String name    ) {
        this.paramValue = paramValue;
        this.name = name;
    }


    public String getParamvalue() {
        return paramValue;
    }

    public void setParamvalue(String paramValue) {
        this.paramValue = paramValue;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}