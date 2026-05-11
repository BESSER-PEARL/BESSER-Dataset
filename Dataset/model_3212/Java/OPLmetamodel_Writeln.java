





import java.util.List;
import java.util.ArrayList;

public class OPLmetamodel_Writeln extends ScriptStatement {

    private String string;
    private String arg;



    public OPLmetamodel_Writeln(
        String string,        String arg    ) {
        super(
        );
        this.string = string;
        this.arg = arg;
    }


    public String getString() {
        return string;
    }

    public void setString(String string) {
        this.string = string;
    }
    public String getArg() {
        return arg;
    }

    public void setArg(String arg) {
        this.arg = arg;
    }


}