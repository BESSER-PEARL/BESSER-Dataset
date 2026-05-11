





import java.util.List;
import java.util.ArrayList;

public class micro_Command extends NamedElement {

    private String commandType;
    private boolean isReplyInfoMany;



    public micro_Command(
        String commandType,        boolean isReplyInfoMany    ) {
        super(
        );
        this.commandType = commandType;
        this.isReplyInfoMany = isReplyInfoMany;
    }


    public String getCommandtype() {
        return commandType;
    }

    public void setCommandtype(String commandType) {
        this.commandType = commandType;
    }
    public boolean getIsreplyinfomany() {
        return isReplyInfoMany;
    }

    public void setIsreplyinfomany(boolean isReplyInfoMany) {
        this.isReplyInfoMany = isReplyInfoMany;
    }


}