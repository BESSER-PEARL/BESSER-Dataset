





import java.util.List;
import java.util.ArrayList;

public class database_Table extends RefTable {

    private String name;



    public database_Table(
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