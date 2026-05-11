





import java.util.List;
import java.util.ArrayList;

public class contentfwk_Product extends Element {






    private contentfwk_OrganizationUnit contentfwk_organizationunit;




    private contentfwk_BusinessArchitecture contentfwk_businessarchitecture;




    private List<contentfwk_OrganizationUnit> contentfwk_organizationunits;


    public contentfwk_Product(
    ) {
        super(
        );
        this.contentfwk_organizationunits = new ArrayList<>();
    }

    public contentfwk_Product(
        ArrayList<contentfwk_OrganizationUnit> contentfwk_organizationunits    ) {
        this.contentfwk_organizationunits = contentfwk_organizationunits;
    }


    public contentfwk_OrganizationUnit getContentfwk_organizationunit() {
        return contentfwk_organizationunit;
    }

    public void setContentfwk_organizationunit(contentfwk_OrganizationUnit contentfwk_organizationunit) {
        this.contentfwk_organizationunit = contentfwk_organizationunit;
    }
    public contentfwk_BusinessArchitecture getContentfwk_businessarchitecture() {
        return contentfwk_businessarchitecture;
    }

    public void setContentfwk_businessarchitecture(contentfwk_BusinessArchitecture contentfwk_businessarchitecture) {
        this.contentfwk_businessarchitecture = contentfwk_businessarchitecture;
    }
    public List<contentfwk_OrganizationUnit> getContentfwk_organizationunits() {
        return contentfwk_organizationunits;
    }

    public void addContentfwk_organizationunit(Contentfwk_organizationunit contentfwk_organizationunit) {
        this.contentfwk_organizationunits.add(contentfwk_organizationunit);
    }

}