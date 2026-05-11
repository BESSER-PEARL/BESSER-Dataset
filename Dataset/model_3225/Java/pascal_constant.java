





import java.util.List;
import java.util.ArrayList;

public class pascal_constant  {

    private String boolean;
    private String sign;
    private String strings;





    private pascal_number pascal_number;




    private pascal_identifier pascal_identifier;




    private pascal_case_label_list pascal_case_label_list;


    public pascal_constant(
        String boolean,        String sign,        String strings    ) {
        this.boolean = boolean;
        this.sign = sign;
        this.strings = strings;
    }


    public String getBoolean() {
        return boolean;
    }

    public void setBoolean(String boolean) {
        this.boolean = boolean;
    }
    public String getSign() {
        return sign;
    }

    public void setSign(String sign) {
        this.sign = sign;
    }
    public String getStrings() {
        return strings;
    }

    public void setStrings(String strings) {
        this.strings = strings;
    }

    public pascal_number getPascal_number() {
        return pascal_number;
    }

    public void setPascal_number(pascal_number pascal_number) {
        this.pascal_number = pascal_number;
    }
    public pascal_identifier getPascal_identifier() {
        return pascal_identifier;
    }

    public void setPascal_identifier(pascal_identifier pascal_identifier) {
        this.pascal_identifier = pascal_identifier;
    }
    public pascal_case_label_list getPascal_case_label_list() {
        return pascal_case_label_list;
    }

    public void setPascal_case_label_list(pascal_case_label_list pascal_case_label_list) {
        this.pascal_case_label_list = pascal_case_label_list;
    }

}