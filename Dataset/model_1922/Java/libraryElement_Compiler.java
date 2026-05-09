





import java.util.List;
import java.util.ArrayList;

public class libraryElement_Compiler  {

    private String language;
    private String vendor;
    private String product;
    private String version;





    private libraryElement_CompilerInfo libraryelement_compilerinfo;


    public libraryElement_Compiler(
        String language,        String vendor,        String product,        String version    ) {
        this.language = language;
        this.vendor = vendor;
        this.product = product;
        this.version = version;
    }


    public String getLanguage() {
        return language;
    }

    public void setLanguage(String language) {
        this.language = language;
    }
    public String getVendor() {
        return vendor;
    }

    public void setVendor(String vendor) {
        this.vendor = vendor;
    }
    public String getProduct() {
        return product;
    }

    public void setProduct(String product) {
        this.product = product;
    }
    public String getVersion() {
        return version;
    }

    public void setVersion(String version) {
        this.version = version;
    }

    public libraryElement_CompilerInfo getLibraryelement_compilerinfo() {
        return libraryelement_compilerinfo;
    }

    public void setLibraryelement_compilerinfo(libraryElement_CompilerInfo libraryelement_compilerinfo) {
        this.libraryelement_compilerinfo = libraryelement_compilerinfo;
    }

}