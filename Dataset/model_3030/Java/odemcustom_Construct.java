





import java.util.List;
import java.util.ArrayList;

public class odemcustom_Construct extends NamedExtension {

    private String concreteSyntax;



    public odemcustom_Construct(
        String concreteSyntax    ) {
        super(
        );
        this.concreteSyntax = concreteSyntax;
    }


    public String getConcretesyntax() {
        return concreteSyntax;
    }

    public void setConcretesyntax(String concreteSyntax) {
        this.concreteSyntax = concreteSyntax;
    }


}