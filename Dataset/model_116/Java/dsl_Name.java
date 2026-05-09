





import java.util.List;
import java.util.ArrayList;

public class dsl_Name  {

    private String ids;





    private dsl_PackageDeclaration dsl_packagedeclaration;




    private dsl_PrimaryPrefix dsl_primaryprefix;




    private dsl_NameList dsl_namelist;




    private dsl_ImportDeclaration dsl_importdeclaration;


    public dsl_Name(
        String ids    ) {
        this.ids = ids;
    }


    public String getIds() {
        return ids;
    }

    public void setIds(String ids) {
        this.ids = ids;
    }

    public dsl_PackageDeclaration getDsl_packagedeclaration() {
        return dsl_packagedeclaration;
    }

    public void setDsl_packagedeclaration(dsl_PackageDeclaration dsl_packagedeclaration) {
        this.dsl_packagedeclaration = dsl_packagedeclaration;
    }
    public dsl_PrimaryPrefix getDsl_primaryprefix() {
        return dsl_primaryprefix;
    }

    public void setDsl_primaryprefix(dsl_PrimaryPrefix dsl_primaryprefix) {
        this.dsl_primaryprefix = dsl_primaryprefix;
    }
    public dsl_NameList getDsl_namelist() {
        return dsl_namelist;
    }

    public void setDsl_namelist(dsl_NameList dsl_namelist) {
        this.dsl_namelist = dsl_namelist;
    }
    public dsl_ImportDeclaration getDsl_importdeclaration() {
        return dsl_importdeclaration;
    }

    public void setDsl_importdeclaration(dsl_ImportDeclaration dsl_importdeclaration) {
        this.dsl_importdeclaration = dsl_importdeclaration;
    }

}