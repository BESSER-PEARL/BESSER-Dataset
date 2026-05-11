





import java.util.List;
import java.util.ArrayList;

public class testintentionsAssistance_DomainDeclaration extends AbstractElement {

    private String name;





    private testintentionsAssistance_Model testintentionsassistance_model;


    public testintentionsAssistance_DomainDeclaration(
        String name    ) {
        super(
        );
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public testintentionsAssistance_Model getTestintentionsassistance_model() {
        return testintentionsassistance_model;
    }

    public void setTestintentionsassistance_model(testintentionsAssistance_Model testintentionsassistance_model) {
        this.testintentionsassistance_model = testintentionsassistance_model;
    }

}