





import java.util.List;
import java.util.ArrayList;

public class relationaldb_Varchar extends PrimitiveType {

    private int length;



    public relationaldb_Varchar(
        int length    ) {
        super(
        );
        this.length = length;
    }


    public int getLength() {
        return length;
    }

    public void setLength(int length) {
        this.length = length;
    }


}