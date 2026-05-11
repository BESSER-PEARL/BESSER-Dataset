





import java.util.List;
import java.util.ArrayList;

public class klangexpr_SendMessage extends Statement {

    private String name;



    public klangexpr_SendMessage(
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


}