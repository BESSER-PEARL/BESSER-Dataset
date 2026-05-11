





import java.util.List;
import java.util.ArrayList;

public class HTML_PARAM  {

    private String name;
    private String paramValue;



    public HTML_PARAM(
        String name,        String paramValue    ) {
        this.name = name;
        this.paramValue = paramValue;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getParamvalue() {
        return paramValue;
    }

    public void setParamvalue(String paramValue) {
        this.paramValue = paramValue;
    }


}