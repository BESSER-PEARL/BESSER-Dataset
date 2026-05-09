





import java.util.List;
import java.util.ArrayList;

public class library_ProductInfo  {

    private String availableDate;
    private String salesCode;
    private String productCode;
    private String underDevelopmentDate;
    private String endOfSalesDate;
    private String endOfSupportDate;





    private List<library_Equipment> library_equipments;




    private List<library_Function> library_functions;




    private List<library_NodeType> library_nodetypes;


    public library_ProductInfo(
        String availableDate,        String salesCode,        String productCode,        String underDevelopmentDate,        String endOfSalesDate,        String endOfSupportDate    ) {
        this.availableDate = availableDate;
        this.salesCode = salesCode;
        this.productCode = productCode;
        this.underDevelopmentDate = underDevelopmentDate;
        this.endOfSalesDate = endOfSalesDate;
        this.endOfSupportDate = endOfSupportDate;
        this.library_equipments = new ArrayList<>();
        this.library_functions = new ArrayList<>();
        this.library_nodetypes = new ArrayList<>();
    }

    public library_ProductInfo(
        String availableDate,        String salesCode,        String productCode,        String underDevelopmentDate,        String endOfSalesDate,        String endOfSupportDate        ArrayList<library_Equipment> library_equipments,        ArrayList<library_Function> library_functions,        ArrayList<library_NodeType> library_nodetypes    ) {
        this.availableDate = availableDate;
        this.salesCode = salesCode;
        this.productCode = productCode;
        this.underDevelopmentDate = underDevelopmentDate;
        this.endOfSalesDate = endOfSalesDate;
        this.endOfSupportDate = endOfSupportDate;
        this.library_equipments = library_equipments;
        this.library_functions = library_functions;
        this.library_nodetypes = library_nodetypes;
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

    public List<library_Equipment> getLibrary_equipments() {
        return library_equipments;
    }

    public void addLibrary_equipment(Library_equipment library_equipment) {
        this.library_equipments.add(library_equipment);
    }
    public List<library_Function> getLibrary_functions() {
        return library_functions;
    }

    public void addLibrary_function(Library_function library_function) {
        this.library_functions.add(library_function);
    }
    public List<library_NodeType> getLibrary_nodetypes() {
        return library_nodetypes;
    }

    public void addLibrary_nodetype(Library_nodetype library_nodetype) {
        this.library_nodetypes.add(library_nodetype);
    }

}