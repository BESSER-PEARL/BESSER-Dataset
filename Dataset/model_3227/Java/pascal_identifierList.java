





import java.util.List;
import java.util.ArrayList;

public class pascal_identifierList  {






    private pascal_programHeading pascal_programheading;




    private pascal_variableDeclaration pascal_variabledeclaration;




    private pascal_identifier pascal_identifier;




    private List<pascal_identifier> pascal_identifiers;


    public pascal_identifierList(
    ) {
        this.pascal_identifiers = new ArrayList<>();
    }

    public pascal_identifierList(
        ArrayList<pascal_identifier> pascal_identifiers    ) {
        this.pascal_identifiers = pascal_identifiers;
    }


    public pascal_programHeading getPascal_programheading() {
        return pascal_programheading;
    }

    public void setPascal_programheading(pascal_programHeading pascal_programheading) {
        this.pascal_programheading = pascal_programheading;
    }
    public pascal_variableDeclaration getPascal_variabledeclaration() {
        return pascal_variabledeclaration;
    }

    public void setPascal_variabledeclaration(pascal_variableDeclaration pascal_variabledeclaration) {
        this.pascal_variabledeclaration = pascal_variabledeclaration;
    }
    public pascal_identifier getPascal_identifier() {
        return pascal_identifier;
    }

    public void setPascal_identifier(pascal_identifier pascal_identifier) {
        this.pascal_identifier = pascal_identifier;
    }
    public List<pascal_identifier> getPascal_identifiers() {
        return pascal_identifiers;
    }

    public void addPascal_identifier(Pascal_identifier pascal_identifier) {
        this.pascal_identifiers.add(pascal_identifier);
    }

}