





import java.util.List;
import java.util.ArrayList;

public class bill  {

    private int tableno;
    private int orderid;
    private String menuid;



    public bill(
        int tableno,        int orderid,        String menuid    ) {
        this.tableno = tableno;
        this.orderid = orderid;
        this.menuid = menuid;
    }


    public int getTableno() {
        return tableno;
    }

    public void setTableno(int tableno) {
        this.tableno = tableno;
    }
    public int getOrderid() {
        return orderid;
    }

    public void setOrderid(int orderid) {
        this.orderid = orderid;
    }
    public String getMenuid() {
        return menuid;
    }

    public void setMenuid(String menuid) {
        this.menuid = menuid;
    }


}