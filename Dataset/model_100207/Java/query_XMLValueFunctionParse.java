





import java.util.List;
import java.util.ArrayList;

public class query_XMLValueFunctionParse extends XMLValueFunction {

    private String whitespaceHandlingOption;
    private String contentOption;



    public query_XMLValueFunctionParse(
        String whitespaceHandlingOption,        String contentOption    ) {
        super(
        );
        this.whitespaceHandlingOption = whitespaceHandlingOption;
        this.contentOption = contentOption;
    }


    public String getWhitespacehandlingoption() {
        return whitespaceHandlingOption;
    }

    public void setWhitespacehandlingoption(String whitespaceHandlingOption) {
        this.whitespaceHandlingOption = whitespaceHandlingOption;
    }
    public String getContentoption() {
        return contentOption;
    }

    public void setContentoption(String contentOption) {
        this.contentOption = contentOption;
    }


}