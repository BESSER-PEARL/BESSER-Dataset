





import java.util.List;
import java.util.ArrayList;

public class pascal_constant  {

    private String boolLiteral;
    private String string;
    private String nil;
    private String name;
    private String opterator;





    private pascal_number pascal_number;




    private pascal_case_label_list pascal_case_label_list;




    private pascal_subrange_type pascal_subrange_type;




    private pascal_subrange_type pascal_subrange_type;




    private pascal_constant_definition pascal_constant_definition;




    private pascal_subrange_type pascal_subrange_type;


    public pascal_constant(
        String boolLiteral,        String string,        String nil,        String name,        String opterator    ) {
        this.boolLiteral = boolLiteral;
        this.string = string;
        this.nil = nil;
        this.name = name;
        this.opterator = opterator;
    }


    public String getBoolliteral() {
        return boolLiteral;
    }

    public void setBoolliteral(String boolLiteral) {
        this.boolLiteral = boolLiteral;
    }
    public String getString() {
        return string;
    }

    public void setString(String string) {
        this.string = string;
    }
    public String getNil() {
        return nil;
    }

    public void setNil(String nil) {
        this.nil = nil;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getOpterator() {
        return opterator;
    }

    public void setOpterator(String opterator) {
        this.opterator = opterator;
    }

    public pascal_number getPascal_number() {
        return pascal_number;
    }

    public void setPascal_number(pascal_number pascal_number) {
        this.pascal_number = pascal_number;
    }
    public pascal_case_label_list getPascal_case_label_list() {
        return pascal_case_label_list;
    }

    public void setPascal_case_label_list(pascal_case_label_list pascal_case_label_list) {
        this.pascal_case_label_list = pascal_case_label_list;
    }
    public pascal_subrange_type getPascal_subrange_type() {
        return pascal_subrange_type;
    }

    public void setPascal_subrange_type(pascal_subrange_type pascal_subrange_type) {
        this.pascal_subrange_type = pascal_subrange_type;
    }
    public pascal_subrange_type getPascal_subrange_type() {
        return pascal_subrange_type;
    }

    public void setPascal_subrange_type(pascal_subrange_type pascal_subrange_type) {
        this.pascal_subrange_type = pascal_subrange_type;
    }
    public pascal_constant_definition getPascal_constant_definition() {
        return pascal_constant_definition;
    }

    public void setPascal_constant_definition(pascal_constant_definition pascal_constant_definition) {
        this.pascal_constant_definition = pascal_constant_definition;
    }
    public pascal_subrange_type getPascal_subrange_type() {
        return pascal_subrange_type;
    }

    public void setPascal_subrange_type(pascal_subrange_type pascal_subrange_type) {
        this.pascal_subrange_type = pascal_subrange_type;
    }

}