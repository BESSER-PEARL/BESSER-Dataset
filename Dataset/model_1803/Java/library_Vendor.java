





import java.util.List;
import java.util.ArrayList;

public class library_Vendor extends Company {






    private List<library_ProductInfo> library_productinfos;


    public library_Vendor(
    ) {
        super(
        );
        this.library_productinfos = new ArrayList<>();
    }

    public library_Vendor(
        ArrayList<library_ProductInfo> library_productinfos    ) {
        this.library_productinfos = library_productinfos;
    }


    public List<library_ProductInfo> getLibrary_productinfos() {
        return library_productinfos;
    }

    public void addLibrary_productinfo(Library_productinfo library_productinfo) {
        this.library_productinfos.add(library_productinfo);
    }

}