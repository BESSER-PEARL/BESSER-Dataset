





import java.util.List;
import java.util.ArrayList;

public class jcl_parameters_MessageLevel extends Parameter {

    private int messages;
    private int statements;



    public jcl_parameters_MessageLevel(
        int messages,        int statements    ) {
        super(
        );
        this.messages = messages;
        this.statements = statements;
    }


    public int getMessages() {
        return messages;
    }

    public void setMessages(int messages) {
        this.messages = messages;
    }
    public int getStatements() {
        return statements;
    }

    public void setStatements(int statements) {
        this.statements = statements;
    }


}