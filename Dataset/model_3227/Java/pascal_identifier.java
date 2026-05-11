





import java.util.List;
import java.util.ArrayList;

public class pascal_identifier  {

    private String identifier;





    private pascal_functionDeclaration pascal_functiondeclaration;




    private pascal_variable pascal_variable;




    private pascal_programHeading pascal_programheading;




    private pascal_procedureDeclaration pascal_proceduredeclaration;




    private pascal_functionDesignator pascal_functiondesignator;


    public pascal_identifier(
        String identifier    ) {
        this.identifier = identifier;
    }


    public String getIdentifier() {
        return identifier;
    }

    public void setIdentifier(String identifier) {
        this.identifier = identifier;
    }

    public pascal_functionDeclaration getPascal_functiondeclaration() {
        return pascal_functiondeclaration;
    }

    public void setPascal_functiondeclaration(pascal_functionDeclaration pascal_functiondeclaration) {
        this.pascal_functiondeclaration = pascal_functiondeclaration;
    }
    public pascal_variable getPascal_variable() {
        return pascal_variable;
    }

    public void setPascal_variable(pascal_variable pascal_variable) {
        this.pascal_variable = pascal_variable;
    }
    public pascal_programHeading getPascal_programheading() {
        return pascal_programheading;
    }

    public void setPascal_programheading(pascal_programHeading pascal_programheading) {
        this.pascal_programheading = pascal_programheading;
    }
    public pascal_procedureDeclaration getPascal_proceduredeclaration() {
        return pascal_proceduredeclaration;
    }

    public void setPascal_proceduredeclaration(pascal_procedureDeclaration pascal_proceduredeclaration) {
        this.pascal_proceduredeclaration = pascal_proceduredeclaration;
    }
    public pascal_functionDesignator getPascal_functiondesignator() {
        return pascal_functiondesignator;
    }

    public void setPascal_functiondesignator(pascal_functionDesignator pascal_functiondesignator) {
        this.pascal_functiondesignator = pascal_functiondesignator;
    }

}