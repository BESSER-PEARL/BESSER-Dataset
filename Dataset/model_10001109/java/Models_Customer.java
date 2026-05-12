





import java.util.List;
import java.util.ArrayList;

public class Models_Customer  {

    private int phoneno;
    private String creditcardinfo;
    private String shippinginfo;
    private String address;
    private String coustomername;
    private boolean deleted;





    private dao_CustomerDao_Interface dao_customerdao_interface;




    private Models_ShoppingCart models_shoppingcart;


    public Models_Customer(
        int phoneno,        String creditcardinfo,        String shippinginfo,        String address,        String coustomername,        boolean deleted    ) {
        this.phoneno = phoneno;
        this.creditcardinfo = creditcardinfo;
        this.shippinginfo = shippinginfo;
        this.address = address;
        this.coustomername = coustomername;
        this.deleted = deleted;
    }


    public int getPhoneno() {
        return phoneno;
    }

    public void setPhoneno(int phoneno) {
        this.phoneno = phoneno;
    }
    public String getCreditcardinfo() {
        return creditcardinfo;
    }

    public void setCreditcardinfo(String creditcardinfo) {
        this.creditcardinfo = creditcardinfo;
    }
    public String getShippinginfo() {
        return shippinginfo;
    }

    public void setShippinginfo(String shippinginfo) {
        this.shippinginfo = shippinginfo;
    }
    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }
    public String getCoustomername() {
        return coustomername;
    }

    public void setCoustomername(String coustomername) {
        this.coustomername = coustomername;
    }
    public boolean getDeleted() {
        return deleted;
    }

    public void setDeleted(boolean deleted) {
        this.deleted = deleted;
    }

    public dao_CustomerDao_Interface getDao_customerdao_interface() {
        return dao_customerdao_interface;
    }

    public void setDao_customerdao_interface(dao_CustomerDao_Interface dao_customerdao_interface) {
        this.dao_customerdao_interface = dao_customerdao_interface;
    }
    public Models_ShoppingCart getModels_shoppingcart() {
        return models_shoppingcart;
    }

    public void setModels_shoppingcart(Models_ShoppingCart models_shoppingcart) {
        this.models_shoppingcart = models_shoppingcart;
    }

}