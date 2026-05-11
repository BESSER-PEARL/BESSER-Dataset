





import java.util.List;
import java.util.ArrayList;

public class micro_Command extends NamedElement {

    private boolean isReplyInfoMany;
    private String commandType;



    public micro_Command(
        boolean isReplyInfoMany,        String commandType    ) {
        super(
        );
        this.isReplyInfoMany = isReplyInfoMany;
        this.commandType = commandType;
    }


    public boolean getIsreplyinfomany() {
        return isReplyInfoMany;
    }

    public void setIsreplyinfomany(boolean isReplyInfoMany) {
        this.isReplyInfoMany = isReplyInfoMany;
    }
    public String getCommandtype() {
        return commandType;
    }

    public void setCommandtype(String commandType) {
        this.commandType = commandType;
    }


}