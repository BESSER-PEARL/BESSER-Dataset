





import java.util.List;
import java.util.ArrayList;

public class pascal_block  {






    private pascal_program pascal_program;




    private pascal_procedureDeclaration pascal_proceduredeclaration;




    private pascal_functionDeclaration pascal_functiondeclaration;


    public pascal_block(
    ) {
    }



    public pascal_program getPascal_program() {
        return pascal_program;
    }

    public void setPascal_program(pascal_program pascal_program) {
        this.pascal_program = pascal_program;
    }
    public pascal_procedureDeclaration getPascal_proceduredeclaration() {
        return pascal_proceduredeclaration;
    }

    public void setPascal_proceduredeclaration(pascal_procedureDeclaration pascal_proceduredeclaration) {
        this.pascal_proceduredeclaration = pascal_proceduredeclaration;
    }
    public pascal_functionDeclaration getPascal_functiondeclaration() {
        return pascal_functiondeclaration;
    }

    public void setPascal_functiondeclaration(pascal_functionDeclaration pascal_functiondeclaration) {
        this.pascal_functiondeclaration = pascal_functiondeclaration;
    }

}