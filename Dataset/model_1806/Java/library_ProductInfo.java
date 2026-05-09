





import java.util.List;
import java.util.ArrayList;

public class library_ProductInfo extends Base {

    private String endOfSalesDate;
    private String productCode;
    private String salesCode;
    private String availableDate;
    private String underDevelopmentDate;
    private String endOfSupportDate;





    private List<library_NodeType> library_nodetypes;


    public library_ProductInfo(
        String endOfSalesDate,        String productCode,        String salesCode,        String availableDate,        String underDevelopmentDate,        String endOfSupportDate    ) {
        super(
        );
        this.endOfSalesDate = endOfSalesDate;
        this.productCode = productCode;
        this.salesCode = salesCode;
        this.availableDate = availableDate;
        this.underDevelopmentDate = underDevelopmentDate;
        this.endOfSupportDate = endOfSupportDate;
        this.library_nodetypes = new ArrayList<>();
    }

    public library_ProductInfo(
        String endOfSalesDate,        String productCode,        String salesCode,        String availableDate,        String underDevelopmentDate,        String endOfSupportDate        ArrayList<library_NodeType> library_nodetypes    ) {
        this.endOfSalesDate = endOfSalesDate;
        this.productCode = productCode;
        this.salesCode = salesCode;
        this.availableDate = availableDate;
        this.underDevelopmentDate = underDevelopmentDate;
        this.endOfSupportDate = endOfSupportDate;
        this.library_nodetypes = library_nodetypes;
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

    public List<library_NodeType> getLibrary_nodetypes() {
        return library_nodetypes;
    }

    public void addLibrary_nodetype(Library_nodetype library_nodetype) {
        this.library_nodetypes.add(library_nodetype);
    }

}