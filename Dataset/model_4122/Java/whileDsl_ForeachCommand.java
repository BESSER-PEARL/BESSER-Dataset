





import java.util.List;
import java.util.ArrayList;

public class whileDsl_ForeachCommand extends Command {

    private String expElement;



    public whileDsl_ForeachCommand(
        String expElement    ) {
        super(
        );
        this.expElement = expElement;
    }


    public String getExpelement() {
        return expElement;
    }

    public void setExpelement(String expElement) {
        this.expElement = expElement;
    }


}