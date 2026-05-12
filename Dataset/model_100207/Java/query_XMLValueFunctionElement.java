





import java.util.List;
import java.util.ArrayList;

public class query_XMLValueFunctionElement extends XMLValueFunction {

    private String returningOption;
    private String elementName;



    public query_XMLValueFunctionElement(
        String returningOption,        String elementName    ) {
        super(
        );
        this.returningOption = returningOption;
        this.elementName = elementName;
    }


    public String getReturningoption() {
        return returningOption;
    }

    public void setReturningoption(String returningOption) {
        this.returningOption = returningOption;
    }
    public String getElementname() {
        return elementName;
    }

    public void setElementname(String elementName) {
        this.elementName = elementName;
    }


}