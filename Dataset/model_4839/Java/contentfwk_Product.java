





import java.util.List;
import java.util.ArrayList;

public class contentfwk_Product extends Element {






    private List<contentfwk_OrganizationUnit> contentfwk_organizationunits;




    private List<contentfwk_Process> contentfwk_processs;




    private contentfwk_Process contentfwk_process;




    private contentfwk_BusinessArchitecture contentfwk_businessarchitecture;




    private contentfwk_OrganizationUnit contentfwk_organizationunit;


    public contentfwk_Product(
    ) {
        super(
        );
        this.contentfwk_organizationunits = new ArrayList<>();
        this.contentfwk_processs = new ArrayList<>();
    }

    public contentfwk_Product(
        ArrayList<contentfwk_OrganizationUnit> contentfwk_organizationunits,        ArrayList<contentfwk_Process> contentfwk_processs    ) {
        this.contentfwk_organizationunits = contentfwk_organizationunits;
        this.contentfwk_processs = contentfwk_processs;
    }


    public List<contentfwk_OrganizationUnit> getContentfwk_organizationunits() {
        return contentfwk_organizationunits;
    }

    public void addContentfwk_organizationunit(Contentfwk_organizationunit contentfwk_organizationunit) {
        this.contentfwk_organizationunits.add(contentfwk_organizationunit);
    }
    public List<contentfwk_Process> getContentfwk_processs() {
        return contentfwk_processs;
    }

    public void addContentfwk_process(Contentfwk_process contentfwk_process) {
        this.contentfwk_processs.add(contentfwk_process);
    }
    public contentfwk_Process getContentfwk_process() {
        return contentfwk_process;
    }

    public void setContentfwk_process(contentfwk_Process contentfwk_process) {
        this.contentfwk_process = contentfwk_process;
    }
    public contentfwk_BusinessArchitecture getContentfwk_businessarchitecture() {
        return contentfwk_businessarchitecture;
    }

    public void setContentfwk_businessarchitecture(contentfwk_BusinessArchitecture contentfwk_businessarchitecture) {
        this.contentfwk_businessarchitecture = contentfwk_businessarchitecture;
    }
    public contentfwk_OrganizationUnit getContentfwk_organizationunit() {
        return contentfwk_organizationunit;
    }

    public void setContentfwk_organizationunit(contentfwk_OrganizationUnit contentfwk_organizationunit) {
        this.contentfwk_organizationunit = contentfwk_organizationunit;
    }

}