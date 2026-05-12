





import java.util.List;
import java.util.ArrayList;

public class CSV  {

    private String cloumn;
    private String row;



    public CSV(
        String cloumn,        String row    ) {
        this.cloumn = cloumn;
        this.row = row;
    }


    public String getCloumn() {
        return cloumn;
    }

    public void setCloumn(String cloumn) {
        this.cloumn = cloumn;
    }
    public String getRow() {
        return row;
    }

    public void setRow(String row) {
        this.row = row;
    }


}