





import java.util.List;
import java.util.ArrayList;

public class syntax_ddl_ReleaseStatement extends DefinitionStatement {

    private String serverName;



    public syntax_ddl_ReleaseStatement(
        String serverName    ) {
        super(
        );
        this.serverName = serverName;
    }


    public String getServername() {
        return serverName;
    }

    public void setServername(String serverName) {
        this.serverName = serverName;
    }


}