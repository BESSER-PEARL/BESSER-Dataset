





import java.util.List;
import java.util.ArrayList;

public class library_ProductInfo extends Base {

    private String endOfSupportDate;
    private String endOfSalesDate;
    private String underDevelopmentDate;
    private String productCode;
    private String availableDate;
    private String salesCode;



    public library_ProductInfo(
        String endOfSupportDate,        String endOfSalesDate,        String underDevelopmentDate,        String productCode,        String availableDate,        String salesCode    ) {
        super(
        );
        this.endOfSupportDate = endOfSupportDate;
        this.endOfSalesDate = endOfSalesDate;
        this.underDevelopmentDate = underDevelopmentDate;
        this.productCode = productCode;
        this.availableDate = availableDate;
        this.salesCode = salesCode;
    }


    public String getEndofsupportdate() {
        return endOfSupportDate;
    }

    public void setEndofsupportdate(String endOfSupportDate) {
        this.endOfSupportDate = endOfSupportDate;
    }
    public String getEndofsalesdate() {
        return endOfSalesDate;
    }

    public void setEndofsalesdate(String endOfSalesDate) {
        this.endOfSalesDate = endOfSalesDate;
    }
    public String getUnderdevelopmentdate() {
        return underDevelopmentDate;
    }

    public void setUnderdevelopmentdate(String underDevelopmentDate) {
        this.underDevelopmentDate = underDevelopmentDate;
    }
    public String getProductcode() {
        return productCode;
    }

    public void setProductcode(String productCode) {
        this.productCode = productCode;
    }
    public String getAvailabledate() {
        return availableDate;
    }

    public void setAvailabledate(String availableDate) {
        this.availableDate = availableDate;
    }
    public String getSalescode() {
        return salesCode;
    }

    public void setSalescode(String salesCode) {
        this.salesCode = salesCode;
    }


}