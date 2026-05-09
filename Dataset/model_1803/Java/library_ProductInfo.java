





import java.util.List;
import java.util.ArrayList;

public class library_ProductInfo extends Base {

    private String productCode;
    private String salesCode;
    private String endOfSalesDate;
    private String availableDate;
    private String underDevelopmentDate;
    private String endOfSupportDate;



    public library_ProductInfo(
        String productCode,        String salesCode,        String endOfSalesDate,        String availableDate,        String underDevelopmentDate,        String endOfSupportDate    ) {
        super(
        );
        this.productCode = productCode;
        this.salesCode = salesCode;
        this.endOfSalesDate = endOfSalesDate;
        this.availableDate = availableDate;
        this.underDevelopmentDate = underDevelopmentDate;
        this.endOfSupportDate = endOfSupportDate;
    }


    public String getProductcode() {
        return productCode;
    }

    public void setProductcode(String productCode) {
        this.productCode = productCode;
    }
    public String getSalescode() {
        return salesCode;
    }

    public void setSalescode(String salesCode) {
        this.salesCode = salesCode;
    }
    public String getEndofsalesdate() {
        return endOfSalesDate;
    }

    public void setEndofsalesdate(String endOfSalesDate) {
        this.endOfSalesDate = endOfSalesDate;
    }
    public String getAvailabledate() {
        return availableDate;
    }

    public void setAvailabledate(String availableDate) {
        this.availableDate = availableDate;
    }
    public String getUnderdevelopmentdate() {
        return underDevelopmentDate;
    }

    public void setUnderdevelopmentdate(String underDevelopmentDate) {
        this.underDevelopmentDate = underDevelopmentDate;
    }
    public String getEndofsupportdate() {
        return endOfSupportDate;
    }

    public void setEndofsupportdate(String endOfSupportDate) {
        this.endOfSupportDate = endOfSupportDate;
    }


}