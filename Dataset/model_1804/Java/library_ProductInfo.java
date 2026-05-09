





import java.util.List;
import java.util.ArrayList;

public class library_ProductInfo extends Base {

    private String salesCode;
    private String availableDate;
    private String endOfSalesDate;
    private String endOfSupportDate;
    private String productCode;
    private String underDevelopmentDate;



    public library_ProductInfo(
        String salesCode,        String availableDate,        String endOfSalesDate,        String endOfSupportDate,        String productCode,        String underDevelopmentDate    ) {
        super(
        );
        this.salesCode = salesCode;
        this.availableDate = availableDate;
        this.endOfSalesDate = endOfSalesDate;
        this.endOfSupportDate = endOfSupportDate;
        this.productCode = productCode;
        this.underDevelopmentDate = underDevelopmentDate;
    }


    public String getSalescode() {
        return salesCode;
    }

    public void setSalescode(String salesCode) {
        this.salesCode = salesCode;
    }
    public String getAvailabledate() {
        return availableDate;
    }

    public void setAvailabledate(String availableDate) {
        this.availableDate = availableDate;
    }
    public String getEndofsalesdate() {
        return endOfSalesDate;
    }

    public void setEndofsalesdate(String endOfSalesDate) {
        this.endOfSalesDate = endOfSalesDate;
    }
    public String getEndofsupportdate() {
        return endOfSupportDate;
    }

    public void setEndofsupportdate(String endOfSupportDate) {
        this.endOfSupportDate = endOfSupportDate;
    }
    public String getProductcode() {
        return productCode;
    }

    public void setProductcode(String productCode) {
        this.productCode = productCode;
    }
    public String getUnderdevelopmentdate() {
        return underDevelopmentDate;
    }

    public void setUnderdevelopmentdate(String underDevelopmentDate) {
        this.underDevelopmentDate = underDevelopmentDate;
    }


}