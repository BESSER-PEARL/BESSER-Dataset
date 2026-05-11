





import java.util.List;
import java.util.ArrayList;

public class sadl_OrderElement  {

    private String order;





    private sadl_ResourceName sadl_resourcename;




    private sadl_OrderList sadl_orderlist;


    public sadl_OrderElement(
        String order    ) {
        this.order = order;
    }


    public String getOrder() {
        return order;
    }

    public void setOrder(String order) {
        this.order = order;
    }

    public sadl_ResourceName getSadl_resourcename() {
        return sadl_resourcename;
    }

    public void setSadl_resourcename(sadl_ResourceName sadl_resourcename) {
        this.sadl_resourcename = sadl_resourcename;
    }
    public sadl_OrderList getSadl_orderlist() {
        return sadl_orderlist;
    }

    public void setSadl_orderlist(sadl_OrderList sadl_orderlist) {
        this.sadl_orderlist = sadl_orderlist;
    }

}