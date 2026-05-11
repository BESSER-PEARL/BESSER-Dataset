





import java.util.List;
import java.util.ArrayList;

public class pp2_Definition extends ExpressionBlock {

    private String className;





    private pp2_DefinitionArgumentList pp2_definitionargumentlist;


    public pp2_Definition(
        String className    ) {
        super(
        );
        this.className = className;
    }


    public String getClassname() {
        return className;
    }

    public void setClassname(String className) {
        this.className = className;
    }

    public pp2_DefinitionArgumentList getPp2_definitionargumentlist() {
        return pp2_definitionargumentlist;
    }

    public void setPp2_definitionargumentlist(pp2_DefinitionArgumentList pp2_definitionargumentlist) {
        this.pp2_definitionargumentlist = pp2_definitionargumentlist;
    }

}