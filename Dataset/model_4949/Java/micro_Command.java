





import java.util.List;
import java.util.ArrayList;

public class micro_Command extends NamedElement {

    private boolean isReplyInfoMany;
    private String commandType;





    private micro_Info micro_info;




    private micro_API micro_api;




    private micro_API micro_api;




    private micro_Step micro_step;


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

    public micro_Info getMicro_info() {
        return micro_info;
    }

    public void setMicro_info(micro_Info micro_info) {
        this.micro_info = micro_info;
    }
    public micro_API getMicro_api() {
        return micro_api;
    }

    public void setMicro_api(micro_API micro_api) {
        this.micro_api = micro_api;
    }
    public micro_API getMicro_api() {
        return micro_api;
    }

    public void setMicro_api(micro_API micro_api) {
        this.micro_api = micro_api;
    }
    public micro_Step getMicro_step() {
        return micro_step;
    }

    public void setMicro_step(micro_Step micro_step) {
        this.micro_step = micro_step;
    }

}