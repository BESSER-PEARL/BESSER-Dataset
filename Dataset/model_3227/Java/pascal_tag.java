





import java.util.List;
import java.util.ArrayList;

public class pascal_tag  {






    private pascal_typeIdentifier pascal_typeidentifier;




    private pascal_identifier pascal_identifier;




    private List<pascal_typeIdentifier> pascal_typeidentifiers;


    public pascal_tag(
    ) {
        this.pascal_typeidentifiers = new ArrayList<>();
    }

    public pascal_tag(
        ArrayList<pascal_typeIdentifier> pascal_typeidentifiers    ) {
        this.pascal_typeidentifiers = pascal_typeidentifiers;
    }


    public pascal_typeIdentifier getPascal_typeidentifier() {
        return pascal_typeidentifier;
    }

    public void setPascal_typeidentifier(pascal_typeIdentifier pascal_typeidentifier) {
        this.pascal_typeidentifier = pascal_typeidentifier;
    }
    public pascal_identifier getPascal_identifier() {
        return pascal_identifier;
    }

    public void setPascal_identifier(pascal_identifier pascal_identifier) {
        this.pascal_identifier = pascal_identifier;
    }
    public List<pascal_typeIdentifier> getPascal_typeidentifiers() {
        return pascal_typeidentifiers;
    }

    public void addPascal_typeidentifier(Pascal_typeidentifier pascal_typeidentifier) {
        this.pascal_typeidentifiers.add(pascal_typeidentifier);
    }

}