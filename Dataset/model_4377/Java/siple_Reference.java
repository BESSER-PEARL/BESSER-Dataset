





import java.util.List;
import java.util.ArrayList;

public class siple_Reference extends Expression {

    private String Name;





    private siple_Declaration siple_declaration;


    public siple_Reference(
        String Name    ) {
        super(
        );
        this.Name = Name;
    }


    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }

    public siple_Declaration getSiple_declaration() {
        return siple_declaration;
    }

    public void setSiple_declaration(siple_Declaration siple_declaration) {
        this.siple_declaration = siple_declaration;
    }

}