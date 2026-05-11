





import java.util.List;
import java.util.ArrayList;

public class rell_VariableDeclaration  {

    private String name;





    private rell_Variable rell_variable;




    private rell_VariableInit rell_variableinit;




    private rell_Attribute rell_attribute;




    private rell_RelAttrubutesList rell_relattrubuteslist;


    public rell_VariableDeclaration(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public rell_Variable getRell_variable() {
        return rell_variable;
    }

    public void setRell_variable(rell_Variable rell_variable) {
        this.rell_variable = rell_variable;
    }
    public rell_VariableInit getRell_variableinit() {
        return rell_variableinit;
    }

    public void setRell_variableinit(rell_VariableInit rell_variableinit) {
        this.rell_variableinit = rell_variableinit;
    }
    public rell_Attribute getRell_attribute() {
        return rell_attribute;
    }

    public void setRell_attribute(rell_Attribute rell_attribute) {
        this.rell_attribute = rell_attribute;
    }
    public rell_RelAttrubutesList getRell_relattrubuteslist() {
        return rell_relattrubuteslist;
    }

    public void setRell_relattrubuteslist(rell_RelAttrubutesList rell_relattrubuteslist) {
        this.rell_relattrubuteslist = rell_relattrubuteslist;
    }

}