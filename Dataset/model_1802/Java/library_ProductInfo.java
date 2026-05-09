





import java.util.List;
import java.util.ArrayList;

public class library_ProductInfo extends Base {

    private String availableDate;
    private String underDevelopmentDate;
    private String endOfSalesDate;
    private String productCode;
    private String endOfSupportDate;
    private String salesCode;





    private List<library_NodeType> library_nodetypes;


    public library_ProductInfo(
        String availableDate,        String underDevelopmentDate,        String endOfSalesDate,        String productCode,        String endOfSupportDate,        String salesCode    ) {
        super(
        );
        this.availableDate = availableDate;
        this.underDevelopmentDate = underDevelopmentDate;
        this.endOfSalesDate = endOfSalesDate;
        this.productCode = productCode;
        this.endOfSupportDate = endOfSupportDate;
        this.salesCode = salesCode;
        this.library_nodetypes = new ArrayList<>();
    }

    public library_ProductInfo(
        String availableDate,        String underDevelopmentDate,        String endOfSalesDate,        String productCode,        String endOfSupportDate,        String salesCode        ArrayList<library_NodeType> library_nodetypes    ) {
        this.availableDate = availableDate;
        this.underDevelopmentDate = underDevelopmentDate;
        this.endOfSalesDate = endOfSalesDate;
        this.productCode = productCode;
        this.endOfSupportDate = endOfSupportDate;
        this.salesCode = salesCode;
        this.library_nodetypes = library_nodetypes;
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
    public String getEndofsalesdate() {
        return endOfSalesDate;
    }

    public void setEndofsalesdate(String endOfSalesDate) {
        this.endOfSalesDate = endOfSalesDate;
    }
    public String getProductcode() {
        return productCode;
    }

    public void setProductcode(String productCode) {
        this.productCode = productCode;
    }
    public String getEndofsupportdate() {
        return endOfSupportDate;
    }

    public void setEndofsupportdate(String endOfSupportDate) {
        this.endOfSupportDate = endOfSupportDate;
    }
    public String getSalescode() {
        return salesCode;
    }

    public void setSalescode(String salesCode) {
        this.salesCode = salesCode;
    }

    public List<library_NodeType> getLibrary_nodetypes() {
        return library_nodetypes;
    }

    public void addLibrary_nodetype(Library_nodetype library_nodetype) {
        this.library_nodetypes.add(library_nodetype);
    }

}