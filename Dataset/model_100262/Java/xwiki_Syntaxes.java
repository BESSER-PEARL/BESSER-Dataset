





import java.util.List;
import java.util.ArrayList;

public class xwiki_Syntaxes extends LinkCollection {

    private String syntax;



    public xwiki_Syntaxes(
        String syntax    ) {
        super(
        );
        this.syntax = syntax;
    }


    public String getSyntax() {
        return syntax;
    }

    public void setSyntax(String syntax) {
        this.syntax = syntax;
    }


}