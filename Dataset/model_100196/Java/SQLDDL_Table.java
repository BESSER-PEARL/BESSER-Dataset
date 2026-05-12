





import java.util.List;
import java.util.ArrayList;

public class SQLDDL_Table extends NamedElement {






    private List<TableElement> tableelements;




    private List<Parameter> parameters;




    private List<ForeignKey> foreignkeys;


    public SQLDDL_Table(
    ) {
        super(
        );
        this.tableelements = new ArrayList<>();
        this.parameters = new ArrayList<>();
        this.foreignkeys = new ArrayList<>();
    }

    public SQLDDL_Table(
        ArrayList<TableElement> tableelements,        ArrayList<Parameter> parameters,        ArrayList<ForeignKey> foreignkeys    ) {
        this.tableelements = tableelements;
        this.parameters = parameters;
        this.foreignkeys = foreignkeys;
    }


    public List<TableElement> getTableelements() {
        return tableelements;
    }

    public void addTableelement(Tableelement tableelement) {
        this.tableelements.add(tableelement);
    }
    public List<Parameter> getParameters() {
        return parameters;
    }

    public void addParameter(Parameter parameter) {
        this.parameters.add(parameter);
    }
    public List<ForeignKey> getForeignkeys() {
        return foreignkeys;
    }

    public void addForeignkey(Foreignkey foreignkey) {
        this.foreignkeys.add(foreignkey);
    }

}