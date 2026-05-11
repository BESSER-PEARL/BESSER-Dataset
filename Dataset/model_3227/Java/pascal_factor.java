





import java.util.List;
import java.util.ArrayList;

public class pascal_factor  {

    private String bool;





    private pascal_factor pascal_factor;




    private pascal_expression pascal_expression;




    private pascal_signedFactor pascal_signedfactor;


    public pascal_factor(
        String bool    ) {
        this.bool = bool;
    }


    public String getBool() {
        return bool;
    }

    public void setBool(String bool) {
        this.bool = bool;
    }

    public pascal_factor getPascal_factor() {
        return pascal_factor;
    }

    public void setPascal_factor(pascal_factor pascal_factor) {
        this.pascal_factor = pascal_factor;
    }
    public pascal_expression getPascal_expression() {
        return pascal_expression;
    }

    public void setPascal_expression(pascal_expression pascal_expression) {
        this.pascal_expression = pascal_expression;
    }
    public pascal_signedFactor getPascal_signedfactor() {
        return pascal_signedfactor;
    }

    public void setPascal_signedfactor(pascal_signedFactor pascal_signedfactor) {
        this.pascal_signedfactor = pascal_signedfactor;
    }

}