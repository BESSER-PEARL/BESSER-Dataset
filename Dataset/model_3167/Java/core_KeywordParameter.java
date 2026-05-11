





import java.util.List;
import java.util.ArrayList;

public class core_KeywordParameter  {

    private String keyword;





    private core_Expression core_expression;




    private core_KeywordMethodCall core_keywordmethodcall;


    public core_KeywordParameter(
        String keyword    ) {
        this.keyword = keyword;
    }


    public String getKeyword() {
        return keyword;
    }

    public void setKeyword(String keyword) {
        this.keyword = keyword;
    }

    public core_Expression getCore_expression() {
        return core_expression;
    }

    public void setCore_expression(core_Expression core_expression) {
        this.core_expression = core_expression;
    }
    public core_KeywordMethodCall getCore_keywordmethodcall() {
        return core_keywordmethodcall;
    }

    public void setCore_keywordmethodcall(core_KeywordMethodCall core_keywordmethodcall) {
        this.core_keywordmethodcall = core_keywordmethodcall;
    }

}