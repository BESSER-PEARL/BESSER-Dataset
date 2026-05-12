





import java.util.List;
import java.util.ArrayList;

public class query_ExpressionWhereEntry extends WhereEntry {

    private String name;



    public query_ExpressionWhereEntry(
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