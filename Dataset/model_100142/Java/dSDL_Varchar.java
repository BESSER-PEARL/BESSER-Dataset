





import java.util.List;
import java.util.ArrayList;

public class dSDL_Varchar extends Type {

    private int length;
    private String varchar;



    public dSDL_Varchar(
        int length,        String varchar    ) {
        super(
        );
        this.length = length;
        this.varchar = varchar;
    }


    public int getLength() {
        return length;
    }

    public void setLength(int length) {
        this.length = length;
    }
    public String getVarchar() {
        return varchar;
    }

    public void setVarchar(String varchar) {
        this.varchar = varchar;
    }


}