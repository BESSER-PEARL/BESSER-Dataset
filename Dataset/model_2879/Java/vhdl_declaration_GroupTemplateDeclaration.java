





import java.util.List;
import java.util.ArrayList;

public class vhdl_declaration_GroupTemplateDeclaration extends Named, declaration_Declaration {

    private String entry;



    public vhdl_declaration_GroupTemplateDeclaration(
        String entry    ) {
        super(
        );
        this.entry = entry;
    }


    public String getEntry() {
        return entry;
    }

    public void setEntry(String entry) {
        this.entry = entry;
    }


}