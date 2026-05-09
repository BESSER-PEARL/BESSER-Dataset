





import java.util.List;
import java.util.ArrayList;

public class library_ProductInfo extends Base {

    private String availableDate;
    private String endOfSupportDate;
    private String salesCode;
    private String underDevelopmentDate;
    private String productCode;
    private String endOfSalesDate;





    private List<library_Equipment> library_equipments;




    private List<library_NodeType> library_nodetypes;




    private List<library_Function> library_functions;


    public library_ProductInfo(
        String availableDate,        String endOfSupportDate,        String salesCode,        String underDevelopmentDate,        String productCode,        String endOfSalesDate    ) {
        super(
        );
        this.availableDate = availableDate;
        this.endOfSupportDate = endOfSupportDate;
        this.salesCode = salesCode;
        this.underDevelopmentDate = underDevelopmentDate;
        this.productCode = productCode;
        this.endOfSalesDate = endOfSalesDate;
        this.library_equipments = new ArrayList<>();
        this.library_nodetypes = new ArrayList<>();
        this.library_functions = new ArrayList<>();
    }

    public library_ProductInfo(
        String availableDate,        String endOfSupportDate,        String salesCode,        String underDevelopmentDate,        String productCode,        String endOfSalesDate        ArrayList<library_Equipment> library_equipments,        ArrayList<library_NodeType> library_nodetypes,        ArrayList<library_Function> library_functions    ) {
        this.availableDate = availableDate;
        this.endOfSupportDate = endOfSupportDate;
        this.salesCode = salesCode;
        this.underDevelopmentDate = underDevelopmentDate;
        this.productCode = productCode;
        this.endOfSalesDate = endOfSalesDate;
        this.library_equipments = library_equipments;
        this.library_nodetypes = library_nodetypes;
        this.library_functions = library_functions;
    }

    public String getAvailabledate() {
        return availableDate;
    }

    public void setAvailabledate(String availableDate) {
        this.availableDate = availableDate;
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
    public String getEndofsalesdate() {
        return endOfSalesDate;
    }

    public void setEndofsalesdate(String endOfSalesDate) {
        this.endOfSalesDate = endOfSalesDate;
    }

    public List<library_Equipment> getLibrary_equipments() {
        return library_equipments;
    }

    public void addLibrary_equipment(Library_equipment library_equipment) {
        this.library_equipments.add(library_equipment);
    }
    public List<library_NodeType> getLibrary_nodetypes() {
        return library_nodetypes;
    }

    public void addLibrary_nodetype(Library_nodetype library_nodetype) {
        this.library_nodetypes.add(library_nodetype);
    }
    public List<library_Function> getLibrary_functions() {
        return library_functions;
    }

    public void addLibrary_function(Library_function library_function) {
        this.library_functions.add(library_function);
    }

}