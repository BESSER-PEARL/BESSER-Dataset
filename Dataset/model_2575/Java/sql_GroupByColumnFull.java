





import java.util.List;
import java.util.ArrayList;

public class sql_GroupByColumnFull extends OrGroupByColumn {

    private String grByInt;



    public sql_GroupByColumnFull(
        String grByInt    ) {
        super(
        );
        this.grByInt = grByInt;
    }


    public String getGrbyint() {
        return grByInt;
    }

    public void setGrbyint(String grByInt) {
        this.grByInt = grByInt;
    }


}