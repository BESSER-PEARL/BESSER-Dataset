





import java.util.List;
import java.util.ArrayList;

public class webApplication_data_Entity extends Named {

    private String numberOfColumns;



    public webApplication_data_Entity(
        String numberOfColumns    ) {
        super(
        );
        this.numberOfColumns = numberOfColumns;
    }


    public String getNumberofcolumns() {
        return numberOfColumns;
    }

    public void setNumberofcolumns(String numberOfColumns) {
        this.numberOfColumns = numberOfColumns;
    }


}