





import java.util.List;
import java.util.ArrayList;

public class domain_CSSMapper extends Mapper {

    private String fakeTypeName;
    private String fakePackageName;
    private String libraryUrl;





    private domain_StyleLibrary domain_stylelibrary;




    private domain_StylesPackage domain_stylespackage;


    public domain_CSSMapper(
        String fakeTypeName,        String fakePackageName,        String libraryUrl    ) {
        super(
        );
        this.fakeTypeName = fakeTypeName;
        this.fakePackageName = fakePackageName;
        this.libraryUrl = libraryUrl;
    }


    public String getFaketypename() {
        return fakeTypeName;
    }

    public void setFaketypename(String fakeTypeName) {
        this.fakeTypeName = fakeTypeName;
    }
    public String getFakepackagename() {
        return fakePackageName;
    }

    public void setFakepackagename(String fakePackageName) {
        this.fakePackageName = fakePackageName;
    }
    public String getLibraryurl() {
        return libraryUrl;
    }

    public void setLibraryurl(String libraryUrl) {
        this.libraryUrl = libraryUrl;
    }

    public domain_StyleLibrary getDomain_stylelibrary() {
        return domain_stylelibrary;
    }

    public void setDomain_stylelibrary(domain_StyleLibrary domain_stylelibrary) {
        this.domain_stylelibrary = domain_stylelibrary;
    }
    public domain_StylesPackage getDomain_stylespackage() {
        return domain_stylespackage;
    }

    public void setDomain_stylespackage(domain_StylesPackage domain_stylespackage) {
        this.domain_stylespackage = domain_stylespackage;
    }

}