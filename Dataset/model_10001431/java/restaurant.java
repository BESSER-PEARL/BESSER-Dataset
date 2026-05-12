





import java.util.List;
import java.util.ArrayList;

public class restaurant  {

    private String Menuid;
    private int tableid;



    public restaurant(
        String Menuid,        int tableid    ) {
        this.Menuid = Menuid;
        this.tableid = tableid;
    }


    public String getMenuid() {
        return Menuid;
    }

    public void setMenuid(String Menuid) {
        this.Menuid = Menuid;
    }
    public int getTableid() {
        return tableid;
    }

    public void setTableid(int tableid) {
        this.tableid = tableid;
    }


}