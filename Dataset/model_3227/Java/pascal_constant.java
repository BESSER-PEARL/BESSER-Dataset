





import java.util.List;
import java.util.ArrayList;

public class pascal_constant extends variant {

    private String sign;
    private String bool;
    private String string;





    private pascal_constantDefinition pascal_constantdefinition;




    private List<pascal_constant> pascal_constants;




    private pascal_constList pascal_constlist;




    private pascal_identifier pascal_identifier;




    private pascal_constList pascal_constlist;


    public pascal_constant(
        String sign,        String bool,        String string    ) {
        super(
        );
        this.sign = sign;
        this.bool = bool;
        this.string = string;
        this.pascal_constants = new ArrayList<>();
    }

    public pascal_constant(
        String sign,        String bool,        String string        ArrayList<pascal_constant> pascal_constants    ) {
        this.sign = sign;
        this.bool = bool;
        this.string = string;
        this.pascal_constants = pascal_constants;
    }

    public String getSign() {
        return sign;
    }

    public void setSign(String sign) {
        this.sign = sign;
    }
    public String getBool() {
        return bool;
    }

    public void setBool(String bool) {
        this.bool = bool;
    }
    public String getString() {
        return string;
    }

    public void setString(String string) {
        this.string = string;
    }

    public pascal_constantDefinition getPascal_constantdefinition() {
        return pascal_constantdefinition;
    }

    public void setPascal_constantdefinition(pascal_constantDefinition pascal_constantdefinition) {
        this.pascal_constantdefinition = pascal_constantdefinition;
    }
    public List<pascal_constant> getPascal_constants() {
        return pascal_constants;
    }

    public void addPascal_constant(Pascal_constant pascal_constant) {
        this.pascal_constants.add(pascal_constant);
    }
    public pascal_constList getPascal_constlist() {
        return pascal_constlist;
    }

    public void setPascal_constlist(pascal_constList pascal_constlist) {
        this.pascal_constlist = pascal_constlist;
    }
    public pascal_identifier getPascal_identifier() {
        return pascal_identifier;
    }

    public void setPascal_identifier(pascal_identifier pascal_identifier) {
        this.pascal_identifier = pascal_identifier;
    }
    public pascal_constList getPascal_constlist() {
        return pascal_constlist;
    }

    public void setPascal_constlist(pascal_constList pascal_constlist) {
        this.pascal_constlist = pascal_constlist;
    }

}