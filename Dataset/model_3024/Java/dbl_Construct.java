





import java.util.List;
import java.util.ArrayList;

public class dbl_Construct extends NamedExtensible {

    private String concreteSyntax;



    public dbl_Construct(
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